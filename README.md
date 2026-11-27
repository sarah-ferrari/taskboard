# TaskBoard v0.1

## Purpose

TaskBoard is a simple CRUD REST API built with FastAPI to create, list, update, and delete tasks.

## Requirements
- Python 3.11+

## Installation

Create a virtual environment and install the dependencies:

```bash
python -m venv .venv

# Windows (PowerShell):
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```


## Environment Variables

Copy `.env.example` to `.env` for local configuration, and **never commit `.env`**:

```bash
cp .env.example .env
```

## Run

Start the local server:

```bash
uvicorn app.main:app --reload
```

Open `[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)` in your browser to access the interactive API documentation (Swagger UI).

## Tests

Run the automated test suite with:

```bash
pytest -v
```

## Project Structure

```text
taskboard/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   └── routers/
│       ├── __init__.py
│       └── tasks.py
├── tests/
│   ├── __init__.py
│   └── test_tasks.py
├── docs/
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```