from google.adk.agents import ParallelAgent, SequentialAgent

from ...worker_agents.query_agent_1.agent import query_agent_1
from ...worker_agents.search_agent_1.agent import search_agent_1
from .synthesizer_agent.agent import synthesizer_agent_query_search

# --- 1. Create Parallel Agent to gather information concurrently ---
ParallelAgent = ParallelAgent(
    name="parallel_agent_query_search",
    sub_agents=[query_agent_1, search_agent_1],
)

# --- 2. Create Sequential Pipeline to gather info in parallel, then synthesize ---
query_search = SequentialAgent(
    name="root_agent_query_search",
    sub_agents=[ParallelAgent, synthesizer_agent_query_search],
)
