from google.adk.agents import ParallelAgent, SequentialAgent

from ...worker_agents.query_agent_2.agent import query_agent_2
from ...worker_agents.rag_agent_2.agent import rag_agent_2
from .synthesizer_agent.agent import synthesizer_agent_query_rag

# --- 1. Create Parallel Agent to gather information concurrently ---
ParallelAgent = ParallelAgent(
    name="parallel_agent_query_rag",
    sub_agents=[query_agent_2, rag_agent_2],
)

# --- 2. Create Sequential Pipeline to gather info in parallel, then synthesize ---
query_rag = SequentialAgent(
    name="root_agent_query_rag",
    sub_agents=[ParallelAgent, synthesizer_agent_query_rag],
)
