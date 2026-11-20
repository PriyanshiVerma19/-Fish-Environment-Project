import requests
from fish_env import simple_agent

API_BASE_URL = "http://127.0.0.1:8000"

print("[START] Running API inference")

for level in ["easy", "medium", "hard"]:
    reset_response = requests.post(
        f"{API_BASE_URL}/reset",
        json={"level": level}
    )
    reset_response.raise_for_status()

    state = reset_response.json()["state"]
    action = simple_agent(state)

    step_response = requests.post(
        f"{API_BASE_URL}/step",
        json={
            "action": action,
            "level": level
        }
    )
    step_response.raise_for_status()

    reward = step_response.json()["reward"]

    print(
        f"[STEP] Level: {level}, State: {state}, "
        f"Action: {action}, Reward: {reward}"
    )

print("[END] Done")