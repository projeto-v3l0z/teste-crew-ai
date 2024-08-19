from crewai import Task

class SearchTasks:
    def task(self, agent, query, dados):
        return Task(
            description=f'Buscar a informação {query} com os seguintes dados: {dados}',
            agent=agent,
            expected_output='A respota deve ser clara e objetiva com base na pergunta do usuário',
        )