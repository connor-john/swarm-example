from .agents import admin_agent
from swarm.repl import run_demo_loop

context_variables = {"topic": "The impacts of LLMs in healthcare"}


def run():
    run_demo_loop(admin_agent, context_variables=context_variables, debug=True)
