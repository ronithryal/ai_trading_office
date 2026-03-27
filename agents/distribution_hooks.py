import os
import datetime

# Helper to format research for specific platforms

def format_for_substack(report_data):
    # Substack likes a conversational intro followed by the deep dive
    return f"""# {report_data['title']}
    
{report_data['summary']}

[Read the full institutional report below]

{report_data['content']}
"""

def format_for_x_thread(report_data):
    # X threads need a hook and numbered tweets
    tweets = [
        f"🧵 NEW RESEARCH: {report_data['title']}\n\n{report_data['hook']}\n\n1/10",
        # ... logic to chunk the report into tweets ...
    ]
    return tweets

def save_client_report(theme, content):
    filename = f"reports/{theme.replace(' ', '_')}_{datetime.date.today()}.md"
    os.makedirs("reports", exist_ok=True)
    with open(filename, "w") as f:
        f.write(content)
    return filename
