from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import TavilySearchTool 

@CrewBase
class StorageIntelCrew():
    """Storage Intelligence Multi-Agent System"""
    
    # These point to the YAML files you just created in the /config folder
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def storage_scout(self) -> Agent:
        return Agent(
            config=self.agents_config['storage_scout'],
            tools=[TavilySearchTool()], # Uses your Tavily search logic
            verbose=True
        )

    @agent
    def technical_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['technical_analyst'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config['research_task'])

    @task
    def analysis_task(self) -> Task:
        return Task(config=self.tasks_config['analysis_task'])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, # Built-in reference to all @agent methods
            tasks=self.tasks,   # Built-in reference to all @task methods
            process=Process.sequential,
            verbose=True
        )
