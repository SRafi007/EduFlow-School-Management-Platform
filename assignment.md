# Python Intern — Task-Home Assignment

**Objective:** Build a professional School Management System (SMS) backend with FastAPI and SQLAlchemy, and a Scraper component that inserts scraped data into a relational database (PostgreSQL/MySQL). Demonstrate OOP (4 pillars), CRUD operations, and basic business logic.

## Part A — Scraper Requirements

• Scrape data from a public website (e.g., books.toscrape.com or quotes.toscrape.com).
• Extract at least: title, URL, category, price/author.
• Provide CLI: `python scrape.py --pages 3 --db .`
• Insert scraped rows into the `scraped_resources` table.
• Save JSON output file `samples/scraped.json`.
• Respect robots.txt and use User-Agent headers.

## Part B — School Management System (SMS) Requirements

• Use FastAPI + SQLAlchemy (or SQLModel).
• Domain classes: Person (abstract), Student, Teacher, Course, Enrollment.
• Demonstrate OOP pillars: Abstraction, Encapsulation, Inheritance, and Polymorphism.
• CRUD endpoints for students, teachers, courses, and enrollments.
• Business rules: prevent duplicate enrollment, enforce course capacity.
• Import scraped data into the `scraped_resources` table via the API endpoint.
• Use environment variables for DB config.
• Include at least 2‒5 pytest tests (enrollment rules, API endpoint, scraper parsing).
• Provide README.md with setup/run instructions and DESIGN.md explaining OOP pillars.

### Example Endpoints:

• `POST /students` — create student
• `GET /students/{id}` — fetch student
• `POST /courses` — create course (with capacity)
• `POST /students/{id}/enroll` — enroll in course (check capacity, duplicates)
• `POST /import/scraped` — import scraped JSON
• `GET /scraped_resources` — list imported scraped rows

## Submission Guidelines:

1. **GitHub:** Create a GitHub repository and upload your project files.
2. **Google Drive Video:** Record a 5-10 minute video explaining the project, then upload it to Google Drive and get a shareable link.
3. **Email:** Send an email to future15@gtrbd.com with the links to your GitHub repository and the Google Drive video.

## Evaluation Criteria (100 pts total):

• Scraper correctness & DB insertion — 30 pts
• OOP design & code quality — 25 pts
• API & business logic — 20 pts
• Tests & documentation — 15 pts
• Bonus (Docker, migrations, extras) — 10 pts