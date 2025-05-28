from google.adk.agents import ParallelAgent, SequentialAgent

from ...worker_agents.query_agent_3.agent import query_agent_3
from ...worker_agents.rag_agent_3.agent import rag_agent_3
from ...worker_agents.search_agent_3.agent import search_agent_3
from .synthesizer_agent.agent import synthesizer_agent_query_rag_search

# --- 1. Create Parallel Agent to gather information concurrently ---
ParallelAgent = ParallelAgent(
    name="parallel_agent_query_rag_search",
    sub_agents=[query_agent_3, rag_agent_3, search_agent_3],
)

# --- 2. Create Sequential Pipeline to gather info in parallel, then synthesize ---
query_rag_search = SequentialAgent(
    name="root_agent_query_rag_search",
    sub_agents=[ParallelAgent, synthesizer_agent_query_rag_search],
)
