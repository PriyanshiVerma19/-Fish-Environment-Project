import random

class AquariumEnvironment:
    def __init__(self):
        # Define different difficulty levels
        self.scenarios = {
            "easy": {"state": {"water": "dirty"}},
            "medium": {"state": {"water": "dirty", "fish": "hungry"}},
            "hard": {"state": {"water": "dirty", "oxygen": "low", "fish": "hungry"}}
        }
        self.current_state = {"water": "dirty"}
    

    def reset(self, level="easy"):
        scenario = self.scenarios[level]
        self.current_state = scenario["state"].copy()
        return self.current_state

    def step(self, action):
        reward = 0

        if action == "clean_tank" and self.current_state.get("water") == "dirty":
            reward += 0.5

        if action == "feed_fish" and self.current_state.get("fish") == "hungry":
            reward += 0.3

        if action == "add_oxygen" and self.current_state.get("oxygen") == "low":
            reward += 0.2

        done = True
        return self.current_state, reward, done, {}


    def state(self):
        return self.current_state


# SIMPLE AGENT
def simple_agent(state):
    if state.get("oxygen") == "low":
        return "add_oxygen"

    if state.get("water") == "dirty":
        return "clean_tank"

    if state.get("fish") == "hungry":
        return "feed_fish"

    return "ignore"


# TASK LIST 
def available_tasks():
    return ["easy", "medium", "hard"]


# RUN TEST
def test_agent():
    env = AquariumEnvironment()
    scores = {}

    for level in available_tasks():
        state = env.reset(level)
        action = simple_agent(state)
        _, reward, _, _ = env.step(action)
        scores[level] = reward

    return scores


if __name__ == "__main__":
    env = AquariumEnvironment()

    for level in available_tasks():
        print("\nLevel:", level)

        state = env.reset(level)
        print("State:", state)

        action = simple_agent(state)
        print("Action:", action)

        _, reward, _, _ = env.step(action)
        print("Score:", reward)

    print("\nFinal Scores:", test_agent())