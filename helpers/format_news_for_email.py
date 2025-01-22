from pydantic_types.final_output import FinalOutput
from datetime import datetime  # Add this line

def format_for_email(final_output: FinalOutput, current_date: datetime) -> str:

    formatted_report_date = current_date.strftime("%B %d, %Y")
    email_body = f"<h1>Welcome to A.I. Tinkers</h1>\n"
    email_body += f"<h2><strong>Date:</strong> {formatted_report_date}</h2>\n"
    email_body += "<hr>\n"

    email_body += f"<p>{final_output.message}</p>\n"

    return email_body