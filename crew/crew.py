from crew.agent import SearchAgents
from crew.task import SearchTasks
from crewai import Crew
from dotenv import load_dotenv

load_dotenv()

class SearchCrew:
    def __init__(self, search, dados):
        self.search = search
        self.dados = dados

    def run(self):
        agents = SearchAgents()
        tasks = SearchTasks()

        agent = agents.agent()
        task = tasks.task(agent, self.search, self.dados)

        crew = Crew(
            agents=[
                agent
            ],
            tasks=[
                task
            ],
            verbose=True
        )

        result = crew.kickoff()
        return result