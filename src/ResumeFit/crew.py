from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from crewai_tools import FileReadTool, SerperDevTool

# from hypermindz.tools import MyCustomTool  # Example custom tool import

@CrewBase
class ResumeFitCrew():
    """Crew to tailor resume for job description and support job application"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def job_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["job_analyst"],
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def resume_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config["resume_evaluator"],
            tools=[FileReadTool("inputs/resume.md")],
            verbose=True
        )

    @agent
    def resume_rewriter(self) -> Agent:
        return Agent(
            config=self.agents_config["resume_rewriter"],
            tools=[FileReadTool("inputs/resume.md")],
            verbose=True
        )

    @agent
    def interview_coach(self) -> Agent:
        return Agent(
            config=self.agents_config["interview_coach"],
            verbose=True
        )

    @agent
    def cover_letter_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["cover_letter_writer"],
            verbose=True
        )

    @task
    def analyze_job_posting(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_job_posting"],
            agent=self.job_analyst()
        )

    @task
    def evaluate_resume(self) -> Task:
        return Task(
            config=self.tasks_config["evaluate_resume"],
            agent=self.resume_evaluator(),
            output_file="outputs/feedback_report.md"
        )

    @task
    def rewrite_resume(self) -> Task:
        return Task(
            config=self.tasks_config["rewrite_resume"],
            agent=self.resume_rewriter(),
            output_file="outputs/updated_resume.md"
        )

    @task
    def prepare_interview(self) -> Task:
        return Task(
            config=self.tasks_config["prepare_interview"],
            agent=self.interview_coach(),
            output_file="outputs/interview_prep.md"
        )

    @task
    def draft_cover_letter(self) -> Task:
        return Task(
            config=self.tasks_config["draft_cover_letter"],
            agent=self.cover_letter_writer(),
            output_file="outputs/cover_letter.md"
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