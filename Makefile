.PHONY: help dev up down restart logs build clean test lint format

help:
	@echo "Available commands:"
	@echo "  make dev      - Start development environment"
	@echo "  make up       - Start containers in background"
	@echo "  make down     - Stop and remove containers"
	@echo "  make restart  - Restart containers"
	@echo "  make logs     - Show container logs"
	@echo "  make build    - Rebuild containers"
	@echo "  make clean    - Remove containers, volumes, and images"
	@echo "  make test     - Run tests"
	@echo "  make lint     - Run linters"
	@echo "  make format   - Format code"

dev:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml up

up:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d

down:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml down

restart:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml restart

logs:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml logs -f

build:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml build

clean:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml down -v --rmi local

test:
	uv run pytest tests/ --cov=app --cov-report=term-missing

lint:
	uv run ruff check app/ tests/

format:
	uv run ruff format app/ tests/
