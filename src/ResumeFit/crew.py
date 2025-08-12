from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

from crewai_tools import FileReadTool, SerperDevTool, ScrapeWebsiteTool

# from hypermindz.tools import MyCustomTool  # Example custom tool import

llm = LLM(model="gpt-4.1-mini", temperature=0.4)

@CrewBase
class ResumeFitCrew():
    """Crew to tailor resume for job description and support job application"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def job_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["job_analyst"],
            tools=[ScrapeWebsiteTool("https://job-boards.greenhouse.io/ctccampusboard/jobs/4545359005")],
            llm=llm,
            verbose=True
        )

    @agent
    def resume_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config["resume_evaluator"],
            # tools=[FileReadTool("inputs/jakes-resume.md")],
            llm=llm,
            verbose=True
        )

    @agent
    def interview_coach(self) -> Agent:
        return Agent(
            config=self.agents_config["interview_coach"],
            llm=llm,
            verbose=True
        )

    @agent
    def cover_letter_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["cover_letter_writer"],
            llm=llm,
            verbose=True
        )
    
    @agent
    def resume_rewriter(self) -> Agent:
        return Agent(
            config=self.agents_config["resume_rewriter"],
            # tools=[FileReadTool("inputs/jakes-resume.md")],
            llm=llm,
            verbose=True
        )

    @task
    def analyze_job_posting(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_job_posting"],
            agent=self.job_analyst(),
            output_file="outputs/analyze_job_posting.md"
        )

    @task
    def evaluate_resume(self) -> Task:
        return Task(
            config=self.tasks_config["evaluate_resume"],
            agent=self.resume_evaluator(),
            output_file="outputs/evaluate_resume.md"
        )

    @task
    def prepare_interview(self) -> Task:
        return Task(
            config=self.tasks_config["prepare_interview"],
            agent=self.interview_coach(),
            output_file="outputs/prepare_interview.md"
        )

    @task
    def draft_cover_letter(self) -> Task:
        return Task(
            config=self.tasks_config["draft_cover_letter"],
            agent=self.cover_letter_writer(),
            output_file="outputs/draft_cover_letter.md"
        )
    
    @task
    def rewrite_resume(self) -> Task:
        return Task(
            config=self.tasks_config["rewrite_resume"],
            agent=self.resume_rewriter(),
            output_file="outputs/rewrite_resume.md"
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=[
                self.analyze_job_posting(),
                self.evaluate_resume(),
                self.rewrite_resume(),
                self.prepare_interview(),
                self.draft_cover_letter(),
            ],
            process=Process.sequential
        )