def analyst_task_description_tmplt(current_date: str, people) -> str:
    return f"""
        Generate a short personalized message for the crowd of attendees of the inaugural A.I. tinkerers event.
        
        # Table of Contents

        - Requirements
        - Research Results

        # Requirements
        
        - Make the messsage short
        - Make the message general to be sent to all the attendees
        
        # Attendees

        {
            "\n".join([f"- {person}" for person in people])
        }
    """