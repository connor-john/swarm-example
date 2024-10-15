from .agents import admin_agent
from swarm.repl import run_demo_loop


def run():
    run_demo_loop(admin_agent, debug=True)
