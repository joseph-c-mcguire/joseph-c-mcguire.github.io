/**
 * Analytics tracking utility for the frontend
 * Sends analytics data to the backend
 */

const BACKEND_URL = import.meta.env.PUBLIC_BACKEND_URL || 'https://joseph-c-mcguire-backend.onrender.com';

interface PageVisitData {
  page: string;
  referrer?: string;
  user_agent?: string;
}

interface ResumeDownloadData {
  source?: string;
}

interface ContactSubmissionData {
  name: string;
  email: string;
  message: string;
  subject?: string;
}

/**
 * Track a page visit
 */
export async function trackPageVisit(page: string): Promise<void> {
  try {
    const data: PageVisitData = {
      page,
      referrer: document.referrer || undefined,
      user_agent: navigator.userAgent,
    };

    await fetch(`${BACKEND_URL}/api/analytics/page-visit`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
  } catch (error) {
    console.error('Failed to track page visit:', error);
  }
}

/**
 * Track a resume download
 */
export async function trackResumeDownload(source?: string): Promise<void> {
  try {
    const data: ResumeDownloadData = {
      source: source || 'website',
    };

    await fetch(`${BACKEND_URL}/api/analytics/resume-download`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
  } catch (error) {
    console.error('Failed to track resume download:', error);
  }
}

/**
 * Track a contact form submission
 */
export async function trackContactSubmission(
  name: string,
  email: string,
  message: string,
  subject?: string
): Promise<void> {
  try {
    const data: ContactSubmissionData = {
      name,
      email,
      message,
      subject,
    };

    await fetch(`${BACKEND_URL}/api/analytics/contact-submission`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
  } catch (error) {
    console.error('Failed to track contact submission:', error);
  }
}
