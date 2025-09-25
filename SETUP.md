
# SETUP.md

##  Project Setup Guide — EduFlow-SMS

This document explains how to set up and run the **EduFlow-SMS** project (API + Scraper + PostgreSQL) locally using **Docker Compose**.

---

## 1.  Prerequisites

Make sure you have the following installed:

* [Python 3.11+](https://www.python.org/downloads/) (for local venv if needed)
* [Docker](https://docs.docker.com/get-docker/)
* [Docker Compose](https://docs.docker.com/compose/install/)

---

## 2.  Clone Repository

```bash
git clone https://github.com/<your-username>/EduFlow-SMS.git
cd EduFlow-SMS
```

---

## 3.  Environment Variables

Create a `.env` file in the root directory:

```env
# PostgreSQL settings
POSTGRES_USER=eduflow
POSTGRES_PASSWORD=eduflow123
POSTGRES_DB=eduflow_db
POSTGRES_HOST=db
POSTGRES_PORT=5432

# API settings
API_PORT=8000
```

---

## 4.  Build & Run with Docker

Run everything with one command:

```bash
docker-compose up --build
```

This will start:

* **PostgreSQL DB** → `localhost:5432`
* **EduFlow API** → `http://localhost:8000`
* **Scraper Service** (runs automatically at startup)

---

## 5.  Database Initialization

Before inserting scraped data, create the tables.

Option 1 — Quick start (dev/demo):

```bash
docker-compose exec api python src/infrastructure/db/init_db.py
```

Option 2 — With migrations (production-ready):

```bash
docker-compose exec api alembic upgrade head
```

---

## 6.  Running the Scraper

To run the scraper manually (e.g., scrape 3 pages and save to DB):

```bash
docker-compose run scraper --pages 3 --db
```

To run without saving to DB (just JSON):

```bash
docker-compose run scraper --pages 3
```

Results are stored at:

```
samples/scraped.json
```

---

## 7.  API Usage

Once the containers are up, visit:

* API Docs → [http://localhost:8000/docs](http://localhost:8000/docs)

Example:

```bash
curl http://localhost:8000/health
```

---

## 8.  Common Issues

* **Relation "scraped_resources" does not exist**
  → Run DB initialization (`init_db.py` or Alembic migration).

* **Port already in use**
  → Stop previous containers:

  ```bash
  docker-compose down
  ```

* **Changes not reflecting**
  → Rebuild with:

  ```bash
  docker-compose up --build
  ```

