# Personal Website + Backend Monorepo

Astro frontend + FastAPI backend deployed to Render.

## Directory Structure

```
.
├── frontend/              # Astro site (static)
│   ├── src/
│   ├── package.json
│   ├── astro.config.mjs
│   └── README.md
├── backend/               # FastAPI server
│   ├── main.py
│   ├── requirements.txt
│   ├── Procfile
│   └── README.md
├── render.yaml           # Render Blueprint
└── README.md
```

## Local Development

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```
Visits `http://localhost:3000`

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
API at `http://localhost:8000`, docs at `/docs`

## Deploy on Render (Blueprint)

1. Push to GitHub.
2. In Render, create a new service from `render.yaml`:
   - Select "Infrastructure as code (IaC)"
   - Paste `render.yaml` contents or connect GitHub and auto-detect.
3. Render deploys two services:
   - **Frontend**: Static site (no dynos required)
   - **Backend**: Web service (standard dyno)
4. Add custom domains in service settings.
5. Configure env vars (`FRONTEND_URL`, etc.) in Render dashboard or Blueprint.

## Notes

- Frontend is static; backend handles dynamic tasks.
- Both services auto-build and deploy on push.
- Backend CORS is configured to allow frontend origin.
- Update `render.yaml` domains to match your setup.

## Frontend README

See [frontend/README.md](frontend/README.md)

## Backend README

See [backend/README.md](backend/README.md)
