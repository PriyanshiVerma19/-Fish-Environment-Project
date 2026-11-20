---
title: Fish Tank Environment API
emoji: 🐟
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
---

# Fish Tank Environment API

A FastAPI project that simulates an aquarium environment. It uses different tank conditions and actions to calculate rewards.

## Features

- Easy, medium, and hard aquarium scenarios
- Aquarium state management
- Actions such as cleaning the tank, feeding fish, and adding oxygen
- Reward-based environment simulation
- FastAPI endpoints
- Local inference testing
- Docker deployment support

## API Endpoints

- `GET /` - Check whether the API is running
- `GET /tasks` - Show available actions
- `GET /state` - Get the current aquarium state
- `POST /reset` - Reset the environment for a selected level
- `POST /step` - Take an action and receive a reward
- `GET /baseline` - View baseline information

## Run Locally

Install the required packages:

```bash
pip install -r requirements.txt