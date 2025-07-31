from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from src.agent_graph import graph_build  # your graph function
from src.save_pdf import save_markdown_as_pdf

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

class TopicRequest(BaseModel):
    topic: str

@app.post("/generate-report", response_class=PlainTextResponse)
async def generate_report(request: TopicRequest):
    try:
        topic = request.topic
        report_data = graph_build(topic)

        # Ensure markdown text is returned directly
        report_text = report_data["report"]
        # print(type(report_text))
        # print(report_data)
        markdown_text = PlainTextResponse(content=report_text, media_type="text/markdown")
        # save_markdown_as_pdf(markdown_text, filename=f"{topic}_report.pdf")
        return PlainTextResponse(content=report_text, media_type="text/markdown")
        
    except Exception as e:
        return PlainTextResponse(status_code=500, content=f"Error: {str(e)}")
