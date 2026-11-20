from fastapi import FastAPI
from fish_env import AquariumEnvironment, simple_agent, available_tasks
from pydantic import BaseModel

class ActionRequest(BaseModel):
    action: str
    level: str

class ResetRequest(BaseModel):
    level: str

class RewardResponse(BaseModel):
    reward: float

app = FastAPI()

env = None

def get_env():
    global env
    if env is None:
        env = AquariumEnvironment()
    return env


@app.get("/")
def home():
    return {"message": "Fish Tank API Running"}


@app.get("/tasks")
def get_tasks():
    return {"tasks": available_tasks()}


@app.get("/state")
def get_state():
    env = get_env()
    return env.state()


@app.post("/reset")
def reset(req: ResetRequest):
    env = get_env()
    state = env.reset(req.level)
    return {"state": state}


@app.post("/step")
def step(req: ActionRequest):
    _, reward, _, _ = get_env().step(req.action)
    return {"reward": reward}

@app.get("/baseline")
def baseline():
    env = get_env()
    results = {}

    for level in available_tasks():
        state = env.reset(level)
        action = simple_agent(state)
        _, reward, _, _ = env.step(action)
        results[level] = reward

    return {"scores": results}