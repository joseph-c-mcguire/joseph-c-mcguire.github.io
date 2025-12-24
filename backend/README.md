# Backend (FastAPI)

## Local Development

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

API will be at `http://localhost:8000`
Docs at `http://localhost:8000/docs`

## Deployment on Render

Render will:
1. Install dependencies: `pip install -r requirements.txt`
2. Run start command: `gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app`

See [../README.md](../README.md) for monorepo docs.
