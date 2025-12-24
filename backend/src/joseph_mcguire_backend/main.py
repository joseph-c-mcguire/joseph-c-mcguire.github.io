from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from datetime import datetime
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Joseph McGuire Backend",
    description="Backend services for personal website",
    version="0.1.0",
)

# Initialize Supabase client
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_PUBLIC_ANON_KEY")

# Only initialize if credentials are available
supabase: Client | None = None
if supabase_url and supabase_key:
    try:
        supabase = create_client(supabase_url, supabase_key)
    except Exception as e:
        print(f"Warning: Failed to initialize Supabase: {e}")
else:
    print("Warning: SUPABASE_URL or SUPABASE_PUBLIC_ANON_KEY not set")

# Enable CORS for frontend requests
origins = [
    "http://localhost:3000",
    "http://localhost:4321",
    "https://joseph-c-mcguire-frontend.onrender.com",
    os.getenv("FRONTEND_URL", "https://www.example.com"),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============= Pydantic Models =============
class PageVisitRequest(BaseModel):
    page: str
    referrer: str | None = None
    user_agent: str | None = None

class ResumeDownloadRequest(BaseModel):
    source: str | None = None

class ContactSubmissionRequest(BaseModel):
    name: str
    email: str
    message: str
    subject: str | None = None

@app.get("/")
async def root():
    return {"message": "Backend is running"}

@app.get("/api/health")
async def health():
    return {"status": "healthy"}

# ============= Analytics Endpoints =============

@app.post("/api/analytics/page-visit")
async def track_page_visit(request: PageVisitRequest):
    """Track page visits"""
    if not supabase:
        return {"success": False, "error": "Supabase not configured"}
    try:
        data = {
            "page": request.page,
            "referrer": request.referrer,
            "user_agent": request.user_agent,
            "visited_at": datetime.utcnow().isoformat()
        }
        response = supabase.table("page_visits").insert(data).execute()
        return {"success": True, "message": "Page visit tracked"}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.post("/api/analytics/resume-download")
async def track_resume_download(request: ResumeDownloadRequest):
    """Track resume downloads"""
    if not supabase:
        return {"success": False, "error": "Supabase not configured"}
    try:
        data = {
            "source": request.source,
            "downloaded_at": datetime.utcnow().isoformat()
        }
        response = supabase.table("resume_downloads").insert(data).execute()
        return {"success": True, "message": "Download tracked"}
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.post("/api/analytics/contact-submission")
async def track_contact_submission(request: ContactSubmissionRequest):
    """Track contact form submissions"""
    if not supabase:
        return {"success": False, "error": "Supabase not configured"}
    try:
        data = {
            "name": request.name,
            "email": request.email,
            "subject": request.subject,
            "message": request.message,
            "submitted_at": datetime.utcnow().isoformat()
        }
        response = supabase.table("contact_submissions").insert(data).execute()
        return {"success": True, "message": "Submission tracked"}
    except Exception as e:
        return {"success": False, "error": str(e)}

# ============= Analytics Report Endpoints =============

@app.get("/api/analytics/page-visits")
async def get_page_visits():
    """Get page visit statistics"""
    if not supabase:
        return {"error": "Supabase not configured"}
    try:
        response = supabase.table("page_visits").select("*").execute()
        visits = response.data
        
        # Calculate statistics
        page_stats = {}
        for visit in visits:
            page = visit["page"]
            page_stats[page] = page_stats.get(page, 0) + 1
        
        return {
            "total_visits": len(visits),
            "visits_by_page": page_stats,
            "raw_data": visits
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/api/analytics/resume-downloads")
async def get_resume_downloads():
    """Get resume download statistics"""
    if not supabase:
        return {"error": "Supabase not configured"}
    try:
        response = supabase.table("resume_downloads").select("*").execute()
        downloads = response.data
        
        # Calculate statistics
        source_stats = {}
        for download in downloads:
            source = download["source"] or "direct"
            source_stats[source] = source_stats.get(source, 0) + 1
        
        return {
            "total_downloads": len(downloads),
            "downloads_by_source": source_stats,
            "raw_data": downloads
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/api/analytics/contact-submissions")
async def get_contact_submissions():
    """Get contact form submissions"""
    if not supabase:
        return {"error": "Supabase not configured"}
    try:
        response = supabase.table("contact_submissions").select("*").execute()
        submissions = response.data
        return {
            "total_submissions": len(submissions),
            "submissions": submissions
        }
    except Exception as e:
        return {"error": str(e)}

# Example endpoint for background tasks
@app.post("/api/tasks")
async def create_task(task: dict):
    """Create and queue a background task"""
    return {"id": "task-123", "status": "queued", "task": task}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
