from google.adk.agents import LlmAgent

GEMINI_MODEL = "gemini-2.0-flash"

synthesizer_agent_query_rag = LlmAgent(
    name="SynthesizerAgent_query_rag",
    model=GEMINI_MODEL,
    description="Synthesizes user question, database query result, and RAG result into a comprehensive report",
    instruction="""You are a User Question Synthesizer.
    
    Your task is to create a comprehensive report by combining information from:
    - User question: {user_question}
    - Result from database query: {database_query_result}
    - Result from RAG: {rag_result}
    
    Create a well-formatted report.
    """,
)
