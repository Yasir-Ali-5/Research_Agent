from langgraph.graph import StateGraph, START, END
from src.planner import planner
from src.outliner import outliner
from src.writer_tools import writer, assign_workers
from src.compiler import report_compiler
from src.type import AgentState

def graph_build(topic):
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner )
    graph.add_node("outliner", outliner )
    graph.add_node("writer", writer )
    graph.add_node("report_compiler", report_compiler )

    graph.add_edge(START, "planner")
    graph.add_edge("planner", "outliner")
    graph.add_conditional_edges(
        "outliner",
        assign_workers,
        ["writer"]
    )

    graph.add_edge("writer", "report_compiler")
    graph.add_edge("report_compiler", END)

    graph.compile()

    agent = graph.compile()

    state = {
        "input": topic
    }
    report = agent.invoke(state)
    # print(type(report))  # Or print(report_data["report"])

    return report
