from google.adk.agents import ParallelAgent, SequentialAgent

from ...worker_agents.rag_agent_1.agent import rag_agent_1
from ...worker_agents.search_agent_2.agent import search_agent_2
from .synthesizer_agent.agent import synthesizer_agent_rag_search

# --- 1. Create Parallel Agent to gather information concurrently ---
ParallelAgent = ParallelAgent(
    name="parallel_agent_rag_search",
    sub_agents=[rag_agent_1, search_agent_2],
)

# --- 2. Create Sequential Pipeline to gather info in parallel, then synthesize ---
rag_search = SequentialAgent(
    name="root_agent_rag_search",
    sub_agents=[ParallelAgent, synthesizer_agent_rag_search],
)
