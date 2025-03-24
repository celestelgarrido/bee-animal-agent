# Python FastAPI Backend Example
App to help users with animal trips

# Technologies
We will use
- Poetry as a package manager (https://python-poetry.org/)
- FastAPI as a framework to develop our back end application (https://fastapi.tiangolo.com/)
- Uvicorn as server to run the application on the laptop (https://www.uvicorn.org/)
- BeeAI as a framework to develop agents (https://github.com/i-am-bee/beeai-framework)

# Run example
1. Prerequisites: Install ollama (https://ollama.com/download) or have a watsonx IBM Cloud 
2. Clone this repo
3. Install in your laptop poetry
```bash
brew install poetry
```
4. Install project dependencies
```bash
poetry install
```
5. Run ollama
```bash
ollama serve
```
6. Download model with ollama
```bash
ollama pull granite3.1-dense:8b
```
7. Activate virtual env
```bash
source .venv/bin/activate
```
8. Run app (other terminal)
```bash
poetry run python -m uvicorn animal.src.main:app --reload
```
