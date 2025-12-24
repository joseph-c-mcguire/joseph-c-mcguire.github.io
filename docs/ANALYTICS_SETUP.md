# Analytics Implementation Guide

This document explains the analytics system implemented for tracking page visits, resume downloads, and contact submissions.

## Overview

Three analytics endpoints have been added to track user interactions:
1. **Page Visit Analytics** - Track which pages users visit
2. **Resume Download Tracking** - Count and log resume downloads
3. **Contact Form Analytics** - Monitor form submissions

## Backend Setup

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Initialize Database Tables

Run the setup script to create the necessary tables in Supabase:

```bash
python setup_database.py
```

This will create three tables:
- `page_visits` - Stores page view events
- `resume_downloads` - Stores resume download events  
- `contact_submissions` - Stores contact form submissions

### 3. Backend Endpoints

#### Track Page Visit
```
POST /api/analytics/page-visit
Content-Type: application/json

{
  "page": "/projects",
  "referrer": "https://google.com",
  "user_agent": "Mozilla/5.0..."
}
```

#### Track Resume Download
```
POST /api/analytics/resume-download
Content-Type: application/json

{
  "source": "projects"
}
```

#### Track Contact Submission
```
POST /api/analytics/contact-submission
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "subject": "Job Inquiry",
  "message": "I'm interested in..."
}
```

#### Get Page Visit Statistics
```
GET /api/analytics/page-visits
```

Response:
```json
{
  "total_visits": 150,
  "visits_by_page": {
    "/": 45,
    "/projects": 60,
    "/experience": 45
  },
  "raw_data": [...]
}
```

#### Get Resume Download Statistics
```
GET /api/analytics/resume-downloads
```

Response:
```json
{
  "total_downloads": 12,
  "downloads_by_source": {
    "projects": 5,
    "experience": 7
  },
  "raw_data": [...]
}
```

#### Get Contact Submissions
```
GET /api/analytics/contact-submissions
```

Response:
```json
{
  "total_submissions": 8,
  "submissions": [...]
}
```

## Frontend Implementation

### 1. Configure Backend URL

Add to `frontend/.env`:
```
PUBLIC_BACKEND_URL=https://joseph-c-mcguire-backend.onrender.com
```

Or for local development:
```
PUBLIC_BACKEND_URL=http://localhost:8000
```

### 2. Import and Use Analytics Utilities

In your Astro components:

```astro
---
import { trackPageVisit, trackResumeDownload, trackContactSubmission } from '@/utils/analytics';

// Track page visit on component load
trackPageVisit('/projects');
---
```

### 3. Track Page Visits

Add this to your `Layout.astro` or main layout component:

```astro
---
import { trackPageVisit } from '@/utils/analytics';

const { page } = Astro.props;

// Track the page visit
trackPageVisit(Astro.url.pathname);
---
```

### 4. Track Resume Downloads

In your component where users download the resume:

```astro
---
import { trackResumeDownload } from '@/utils/analytics';

const handleDownload = async (source: string) => {
  await trackResumeDownload(source);
  // Trigger the download
  window.location.href = '/2025-11-10_milliman.pdf';
};
---

<button onclick={`handleDownload('experience')`}>
  Download Resume
</button>
```

### 5. Track Contact Submissions

In your contact form:

```astro
---
import { trackContactSubmission } from '@/utils/analytics';

const handleSubmit = async (e: Event) => {
  const form = e.target as HTMLFormElement;
  const formData = new FormData(form);
  
  await trackContactSubmission(
    formData.get('name') as string,
    formData.get('email') as string,
    formData.get('message') as string,
    formData.get('subject') as string
  );
  
  // Submit the form
};
---
```

## Data Models

### page_visits
```sql
- id (BIGSERIAL PRIMARY KEY)
- page (VARCHAR 255)
- referrer (VARCHAR 255)
- user_agent (TEXT)
- visited_at (TIMESTAMP)
- created_at (TIMESTAMP)
```

### resume_downloads
```sql
- id (BIGSERIAL PRIMARY KEY)
- source (VARCHAR 255)
- downloaded_at (TIMESTAMP)
- created_at (TIMESTAMP)
```

### contact_submissions
```sql
- id (BIGSERIAL PRIMARY KEY)
- name (VARCHAR 255)
- email (VARCHAR 255)
- subject (VARCHAR 255)
- message (TEXT)
- submitted_at (TIMESTAMP)
- created_at (TIMESTAMP)
```

## Next Steps

1. Run the database setup script in the backend directory
2. Add the `PUBLIC_BACKEND_URL` environment variable to your frontend
3. Import analytics functions in your Astro components
4. Call tracking functions at appropriate points in your app
5. Monitor analytics at the `/api/analytics/*` endpoints

## Tips

- Analytics calls are non-blocking and won't affect page performance
- Failed analytics requests are logged to console but don't break functionality
- Use the statistics endpoints to build an admin dashboard
- Add error handling and retry logic if needed for critical analytics
