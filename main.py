from src.agent_graph import graph_build


topic = input("Enter Topic for research :")
report = graph_build(topic)
print(report)