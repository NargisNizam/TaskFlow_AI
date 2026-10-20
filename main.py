
import logging
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(
    title="TaskFlow AI",
    description="AI-powered task organization assistant",
    version="1.0.0",
)

app.mount(
    "/static",
    StaticFiles(directory=str(STATIC_DIR)),
    name="static",
)


class OrganizeRequest(BaseModel):
    user_input: str = Field(min_length=1, max_length=5000)


@app.get("/")
def home():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/organize")
def organize_tasks(request: OrganizeRequest):
    user_input = request.user_input.strip()

    if not user_input:
        raise HTTPException(
            status_code=400,
            detail="Please enter some tasks.",
        )

    try:
        # Import the graph when a request is received.
        from src.graph import build_graph

        graph = build_graph()

        result = graph.invoke({
            "user_input": user_input,
            "tasks": [],
            "prioritized_tasks": [],
            "formatted_result": "",
        })

        return {
            "tasks": result.get("prioritized_tasks", []),
            "formatted_result": result.get("formatted_result", ""),
        }

    except Exception:
        logger.exception("TaskFlow AI failed to organize tasks.")

        raise HTTPException(
            status_code=500,
            detail=(
                "AI could not organize your tasks. "
                "Please check your Groq API key and the terminal error."
            ),
        )
