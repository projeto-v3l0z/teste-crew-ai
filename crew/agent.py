from crewai import Agent

class SearchAgents: 
    def agent(self):
        return Agent(
            role='Analista de dados',
            goal='Facilitar a compreensão de informações',
            backstory='Especialista em análise de dados que retorna informações relevantes para o usuário',
            verbose=True
        )
