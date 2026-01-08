from fastapi import FastAPI
from pydantic import BaseModel
from my_agent.agent import root_agent

app = FastAPI(title="Fireworks Agent API")

# Request model
class QueryRequest(BaseModel):
    query: str

# Health check
@app.get("/")
def health_check():
    return {"status": "ok", "message": "Agent API running"}

# Query endpoint
@app.post("/ask")
def ask_agent(request: QueryRequest):
    result = root_agent.run(request.query)
    return result
