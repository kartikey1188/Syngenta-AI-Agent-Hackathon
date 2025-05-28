from datetime import datetime
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
import sys
import os
from google.adk.tools.tool_context import ToolContext

# Adding the backend directory to the Python path to import the database session
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from app.models.sqlalchemy import SessionLocal


def get_query_output(query_input: str, tool_context: ToolContext):
    """
    Executes a PostgreSQL query against the database and returns the results.
    
    This tool allows an AI agent to run SQL queries on the PostgreSQL database to retrieve, 
    analyze, or manipulate data. It accepts any valid PostgreSQL SQL statement including 
    SELECT, INSERT, UPDATE, DELETE, and complex queries with JOINs, aggregations, 
    subqueries, etc. The tool handles database connections automatically and provides 
    comprehensive error handling.
    
    Args:
        query_input (str): A valid PostgreSQL SQL query string to execute against the database.
                          Examples: "SELECT * FROM users", "SELECT COUNT(*) FROM users WHERE role = 'admin'",
                          "INSERT INTO users (name, email) VALUES ('John', 'john@example.com')"
    
    Returns:
        dict: A dictionary containing the query results with the key "query_output".
              For SELECT queries: Returns list of dictionaries representing rows.
              For INSERT/UPDATE/DELETE: Returns success message with affected row count.
              For errors: Returns error message with details.
    
    Note: This tool provides direct database access, so queries should be carefully constructed
    to avoid unintended data modifications or performance issues.
    """
    try:
        tool_context.state["raw_sql"] = query_input
    except Exception as e:
        return {
            "error": f"Error setting raw SQL in state: {str(e)}"
        }
    print(f"Executing query: {query_input}")
    db = SessionLocal()
    try:
        # Executing the query using SQLAlchemy's text() for raw SQL
        result = db.execute(text(query_input))
        
        # Checking if this is a SELECT query (returns results)
        if query_input.strip().upper().startswith('SELECT'):
            # Fetching all results and convert to list of dictionaries
            rows = result.fetchall()
            columns = result.keys()
            query_output = [dict(zip(columns, row)) for row in rows]
        else:
            # For INSERT, UPDATE, DELETE queries
            db.commit()
            affected_rows = result.rowcount
            query_output = f"Query executed successfully. {affected_rows} row(s) affected."
            
    except SQLAlchemyError as e:
        # Handling database-specific errors
        db.rollback()
        query_output = f"Database error: {str(e)}"
    except Exception as e:
        # Handling any other errors
        db.rollback()
        query_output = f"Error executing query: {str(e)}"
    finally:
        db.close()

    
    return {
        "query_output": query_output,
    }
