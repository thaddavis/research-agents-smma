def research_task_description_tmplt(link: str, date) -> str:
        return f"""
            Conduct research about the attendees of a meetup in Miami called A.I. tinkerers: { link }
            You may crawl this link up to maximum one level deep.
            Make sure all the information is accurate.
            
            Requirements:
            - Do not hallucinate or fabricate information or sources
            - Focus on information
            - Report all information in english
        """