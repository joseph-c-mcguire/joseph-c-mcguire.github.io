"""
Database setup script for analytics tables in Supabase
Run this once to create the required tables
"""
import os
from dotenv import load_dotenv
from supabase import create_client, Client
import psycopg2
from psycopg2 import sql

load_dotenv()

# Get the connection string from environment
connection_string = os.getenv("SUPABASE_CONNECTION_STRING")

if not connection_string:
    print("Error: SUPABASE_CONNECTION_STRING not found in .env")
    exit(1)

try:
    # Connect to the database
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    
    # Create page_visits table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS page_visits (
        id BIGSERIAL PRIMARY KEY,
        page VARCHAR(255) NOT NULL,
        referrer VARCHAR(255),
        user_agent TEXT,
        visited_at TIMESTAMP DEFAULT NOW(),
        created_at TIMESTAMP DEFAULT NOW()
    );
    """)
    print("✓ Created page_visits table")
    
    # Create resume_downloads table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resume_downloads (
        id BIGSERIAL PRIMARY KEY,
        source VARCHAR(255),
        downloaded_at TIMESTAMP DEFAULT NOW(),
        created_at TIMESTAMP DEFAULT NOW()
    );
    """)
    print("✓ Created resume_downloads table")
    
    # Create contact_submissions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contact_submissions (
        id BIGSERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        subject VARCHAR(255),
        message TEXT NOT NULL,
        submitted_at TIMESTAMP DEFAULT NOW(),
        created_at TIMESTAMP DEFAULT NOW()
    );
    """)
    print("✓ Created contact_submissions table")
    
    # Create indexes for better query performance
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_page_visits_page ON page_visits(page);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_page_visits_visited_at ON page_visits(visited_at);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_resume_downloads_source ON resume_downloads(source);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_contact_submissions_email ON contact_submissions(email);")
    print("✓ Created indexes")
    
    conn.commit()
    cursor.close()
    conn.close()
    print("\n✅ Database setup completed successfully!")
    
except Exception as e:
    print(f"❌ Error setting up database: {e}")
    exit(1)
