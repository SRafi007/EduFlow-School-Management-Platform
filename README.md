# EduFlow SMS – School Management System

A production-ready backend project built with **FastAPI**, **SQLAlchemy**, and **Python OOP**. Assignment project for demonstrating **scraping, APIs, OOP design, business rules, and testing**.

## Overview

EduFlow SMS is a **School Management System backend** with:
* **Scraper** → collects external data (books/quotes) into DB + JSON.
* **School Management System (SMS)** → manages students, teachers, courses, enrollments.
* **Business rules** → prevent duplicate enrollments, enforce course capacity.
* **API endpoints** → CRUD operations + scraper data import.
* **Tests** → unit + integration with pytest.

This project is designed with **clean architecture principles** (domain, infrastructure, application, interfaces).

## Project Structure

```
eduflow-sms/
├── docker/               # Docker setup (API + DB)
├── src/
│   ├── domain/           # OOP models (Person, Student, Teacher, Course, Enrollment)
│   ├── infrastructure/   # DB (SQLAlchemy) + scraper implementation
│   ├── application/      # Business rules (enrollment, capacity checks)
│   ├── interfaces/       # FastAPI routes + CLI
│   ├── utils/            # exceptions, logger
│   └── config/           #  settings
├── tests/                # Unit + integration tests
├── samples/              # Example scraped.json, seed data
├── docs/                 # DESIGN.md (OOP pillars, architecture)
├── README.md             # Setup + usage instructions
├── requirements.txt      # Dependencies
├── .env.example          # Environment variables
└── docker-compose.yml    # API + DB orchestration
```

## Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/yourusername/eduflow-sms.git
cd eduflow-sms
```

### 2. Setup Environment
Create a virtual environment:

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

Install dependencies:

```
pip install -r requirements.txt
```

Copy env file:

```
cp .env.example .env
```

Edit `.env` with your database settings:

```
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/eduflow
```

### 3. Run with Docker (Recommended)
Start API + PostgreSQL:

```
docker-compose up --build
```

### 4. Run Database Migrations

```
alembic upgrade head
```

### 5. Start FastAPI App

```
uvicorn src.interfaces.api.main:app --reload
```

API will be available at: http://localhost:8000/docs

## Scraper Usage

Run scraper via CLI:

```
python -m src.infrastructure.scraper.scrape --pages 3 --db
```

* `--pages 3` → scrape 3 pages
* `--db` → save to DB
* Output saved to `samples/scraped.json`

## API Endpoints

Some examples:

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/students` | Create a student |
| `GET` | `/students/{id}` | Get student details |
| `POST` | `/courses` | Create course with capacity |
| `POST` | `/students/{id}/enroll` | Enroll student in course |
| `POST` | `/import/scraped` | Import scraped JSON into DB |
| `GET` | `/scraped_resources` | List imported scraped data |

## Business Rules

* A student **cannot enroll twice** in the same course.
* Enrollment will fail if the course is **already full**.

## Running Tests

Run pytest:

```
pytest -v
```

Run only integration tests:

```
pytest tests/integration -v
```

Run coverage report:

```
pytest --cov=src
```

## Documentation

* `README.md` → setup & usage guide (this file)
* `docs/DESIGN.md` → explains OOP pillars + architecture

## Submission Requirements

1. **GitHub Repo** → Upload this project.
2. **Demo Video (5–10 min)** → Walk through code + demo API/scraper.
3. **Email** → Send repo + video link to `future15@gtrbd.com`.

## Evaluation Criteria

* **Scraper correctness & DB insertion** → 30 pts
* **OOP design & code quality** → 25 pts
* **API & business logic** → 20 pts
* **Tests & documentation** → 15 pts
* **Bonus (Docker, migrations, extras)** → 10 pts

Built with **FastAPI + SQLAlchemy + Clean Architecture** to showcase production-ready skills.