from typing import TypedDict, Annotated
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from gemini_module import generate_gemini_response
from serper_module import fetch_serper_results
from tavily_module import fetch_tavily_summary


# Define input/output schema
class SmartOpsState(TypedDict):
    query: str
    serper: str
    tavily: str
    final: str


def run_conversation(user_input: str):
    # Step 1 - Use Serper API
    def step_one(state: SmartOpsState) -> SmartOpsState:
        results = fetch_serper_results(state["query"])
        return {"query": state["query"], "serper": str(results)}
    
    # Step 2 - Use Tavily API
    def step_two(state: SmartOpsState) -> SmartOpsState:
        summary = fetch_tavily_summary(state["query"])
        return {"query": state["query"], "serper": state["serper"], "tavily": summary}
    
    # Step 3 - Use Gemini API to generate strategy
    def step_three(state: SmartOpsState) -> SmartOpsState:
        prompt = f"User asked: {state['query']}\n\nSearch Results: {state['serper']}\n\nSummary: {state['tavily']}"
        response = generate_gemini_response(prompt, "")
        return {"query": state["query"], "serper": state["serper"], "tavily": state["tavily"], "final": response}
    

    # Build LangGraph flow
    builder = StateGraph(SmartOpsState)
    builder.add_node("step_one", step_one)
    builder.add_node("step_two", step_two)
    builder.add_node("step_three", step_three)

    builder.set_entry_point("step_one")
    builder.add_edge("step_one", "step_two")
    builder.add_edge("step_two", "step_three")
    builder.set_finish_point("step_three")

    graph = builder.compile()
    result = graph.invoke({"query": user_input})
    return result["final"]

    


