# ===============================
# EduFlow SMS - Makefile
# Simplify common tasks
# ===============================

# Variables
DOCKER_COMPOSE = docker-compose -f docker/docker-compose.yml

# ===============================
# Core Commands
# ===============================

.PHONY: up
up: ## Start API + DB
	$(DOCKER_COMPOSE) up --build -d

.PHONY: down
down: ## Stop all containers
	$(DOCKER_COMPOSE) down

.PHONY: logs
logs: ## Tail API logs
	$(DOCKER_COMPOSE) logs -f api

.PHONY: db-logs
db-logs: ## Tail DB logs
	$(DOCKER_COMPOSE) logs -f db

.PHONY: scraper
scraper: ## Run scraper with default args
	$(DOCKER_COMPOSE) run scraper

.PHONY: scrape-pages
scrape-pages: ## Run scraper with custom pages (default: 5)
	$(DOCKER_COMPOSE) run scraper python src/infrastructure/scraper/scrape.py --pages 5 --db

.PHONY: migrate
migrate: ## Run Alembic migrations
	$(DOCKER_COMPOSE) run api alembic upgrade head

.PHONY: test
test: ## Run pytest inside API container
	$(DOCKER_COMPOSE) run api pytest -v

.PHONY: lint
lint: ## Run flake8 linting
	$(DOCKER_COMPOSE) run api flake8 src

.PHONY: clean
clean: ## Remove containers, volumes, and logs
	$(DOCKER_COMPOSE) down -v
	rm -rf logs/*


#
# ==============================================================================
# Example Usage:
#
# Start API + DB:
# make up
#
# Run scraper (default 3 pages, DB insert):
# make scraper
#
# Run scraper with 5 pages:
# make scrape-pages
#
# View API logs:
# make logs
#
# Run tests:
# make test
#
# Shut everything down:
# make down
#
# Clean everything (DB + volumes + logs):
# make clean
# ==============================================================================
#