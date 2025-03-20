# Python FastAPI Backend Template
App to help users with animal trips

# Technologies
We will use
- Poetry as a package manager
- FastAPI as a framework to develop our application
- Uvicorn as server to run the application on the laptop 

# Dev
1. Clone this repo
2. Install in your laptop poetry 
pip install poetry
3. Install project dependencies
poetry install
4. Run app
poetry run python -m uvicorn animal.src.main:app --reload
