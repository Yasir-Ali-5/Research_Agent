from langchain_core.messages import HumanMessage, AIMessage
from src.type import AgentState, Outline
from src.model_config import model

def outliner(state:AgentState):
    section_list = state["report_plan"]
    prompt = [
        AIMessage(content="""You are an expert report writer.
                              Your job is to look at the provided sections and sub section and make a proper table of content for the report
                              Do not include any extra text from yourself"""),
        HumanMessage(content=str(section_list))
    ]

    model2 = model.with_structured_output(Outline)

    outline = model2.invoke(prompt)
    return {
        "outline": outline.outline
    }