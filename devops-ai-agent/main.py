from fastapi import FastAPI
from system import get_system_info
from git_ops import clone_repo
from deploy import deploy_app
from agent import ai_think

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Autonomous DevOps AI Agent Running"}

@app.get("/system")
def system():
    return get_system_info()

@app.post("/chat")
def chat(prompt: str):
    return {"ai_response": ai_think(prompt)}

@app.post("/git/clone")
def git_clone(repo_url: str):
    return clone_repo(repo_url)

@app.post("/deploy")
def deploy():
    return deploy_app()

@app.post("/agent")
def autonomous_agent(task: str):
    reasoning = ai_think(f"You are DevOps AI. Task: {task}")
    return {"task": task, "ai_decision": reasoning}
