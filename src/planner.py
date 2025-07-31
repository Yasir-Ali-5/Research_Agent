from langchain_core.messages import HumanMessage, AIMessage
from src.type import AgentState, Sections
from src.model_config import model

def planner(state:AgentState):
    input = state["input"]
    prompt = [
        AIMessage(content="You are an expert report writer. Your job is to look at the user query and generate a comprehensive outline of the report abou the query"),
        HumanMessage(content=input)
    ]

    model2 = model.with_structured_output(Sections)

    res = model2.invoke(prompt)
    # print(res)
    # print(res["sections"])
    return {
        "report_plan": res.sections
    }