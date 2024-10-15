from swarm import Agent
from dotenv import load_dotenv

import os
from datetime import datetime

load_dotenv()


def transfer_to_researcher():
    return researcher_agent


def transfer_to_planner():
    return planner_agent


def transfer_to_writer():
    return writer_agent


def transfer_to_editor():
    return editor_agent


def transfer_to_admin():
    return admin_agent


def complete_blog_post(title, content):
    # Create a valid filename from the title
    filename = title.lower().replace(" ", "-") + ".md"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Blog post '{title}' has been written to {filename}")
    return "Task completed"


def admin_instructions(context_variables):
    topic = context_variables.get("topic", "No topic provided")
    return f"""You are the Admin Agent overseeing the blog post project on the topic: '{topic}'.
Your responsibilities include initiating the project, providing guidance, and reviewing the final content.
Once you've set the topic, call the function to transfer to the planner agent."""


def planner_instructions(context_variables):
    topic = context_variables.get("topic", "No topic provided")
    return f"""You are the Planner Agent. Based on the following topic: '{topic}'
Organize the content into topics and sections with clear headings that will each be individually researched as points in the greater blog post.
Once the outline is ready, call the researcher agent. """


def researcher_instructions(context_variables):
    return """You are the Researcher Agent. your task is to provide dense context and information on the topics outlined by the previous planner agent.
This research will serve as the information that will be formatted into a body of a blog post. Provide comprehensive research like notes for each of the sections outlined by the planner agent.
Once your research is complete, transfer to the writer agent"""


def writer_instructions(context_variables):
    return """You are the Writer Agent. using the prior information write a clear blog post following the outline from the planner agent. 
    Summarise and include as much information relevant from the research into the blog post.
    The blog post should be quite large as the context the context provided should be quite dense.
Write clear, engaging content for each section.
Once the draft is complete, call the function to transfer to the Editor Agent."""


def editor_instructions(context_variables):
    return """You are the Editor Agent. Review and edit th prior blog post completed by the writer agent.
Make necessary corrections and improvements.
Once editing is complete, call the function to complete the blog post"""


admin_agent = Agent(
    name="Admin Agent",
    instructions=admin_instructions,
    functions=[transfer_to_planner],
)

planner_agent = Agent(
    name="Planner Agent",
    instructions=planner_instructions,
    functions=[transfer_to_researcher],
)

researcher_agent = Agent(
    name="Researcher Agent",
    instructions=researcher_instructions,
    functions=[transfer_to_writer],
)

writer_agent = Agent(
    name="Writer Agent",
    instructions=writer_instructions,
    functions=[transfer_to_editor],
)

editor_agent = Agent(
    name="Editor Agent",
    instructions=editor_instructions,
    functions=[complete_blog_post],
)
