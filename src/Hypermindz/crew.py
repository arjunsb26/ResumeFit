from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from crewai_tools import FileReadTool, SerperDevTool

# from hypermindz.tools import MyCustomTool  # Example custom tool import


@CrewBase
class HypermindzCrew():
	# Hypermindz crew template
	
	def __init__(self, link):
		self.link = link

	agents_config = "config/agents.yaml"
	tasks_config = "config/tasks.yaml"

	@agent
	def resume_grader_agent(self) -> Agent:
		return Agent( 
			config = self.agents_config["resume_grader_agent"],
			tools = [FileReadTool("inputs/jakes-resume.md")],
			# tools = [PDFSearchTool(pdf = "inputs/jakes-resume.pdf")],
			verbose = True
		)
	
	@agent
	def job_tailor_agent(self) -> Agent:
		return Agent(
			config = self.agents_config["job_tailor"],
			tools = [ScrapeWebsiteTool(website_url = "https://job-boards.greenhouse.io/ctccampusboard/jobs/4545359005")],
			verbose = True
		)

	@task
	def grade_resume_task(self) -> Task:
		return Task(
			config = self.tasks_config["grade_resume_task"],
			agent = self.resume_grader_agent(),
			output_file = "outputs/feedback.txt"
		)

	@crew
	def crew(self) -> Crew:
		# Creates a general crew setup
		return Crew(
			agents = self.agents,
			tasks = self.tasks,
			process = Process.sequential,
			verbose = True,
			# process = Process.hierarchical,
		)
