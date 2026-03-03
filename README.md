# Building_Agentic_AI
Its a repo to build and work upon my knowledge and understanding


## Codes

uvicorn api.main:app --reload
streamlit run streamlit_app.py

docker build -t fastapi-agent .  [#This will create a Docker image named fastapi-agent.]

docker run -d --name my_fastapi_agent -p 8000:8000 --env-file .env fastapi-agent
[# -d → Run in detached mode

--name my_fastapi_agent → Container name

-p 8000:8000 → Map host port 8000 to container port 8000

--env-file .env → Load your Fireworks API key from .env]