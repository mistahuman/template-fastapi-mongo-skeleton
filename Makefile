PROJECT_NAME := myappname
BACKEND_CONTAINER := $(PROJECT_NAME)_backend
BACKEND_ID := $(shell docker ps -qf "name=$(BACKEND_CONTAINER)")

.PHONY: help install dev run build start stop restart status clean logs shell-backend test ui

help:
	@echo "Available commands:"
	@echo "  make install          - Install dependencies"
	@echo "  make dev              - Start dev mode"
	@echo "  make run              - Build and start all containers"
	@echo "  make build            - Build all images"
	@echo "  make start            - Start all containers"
	@echo "  make stop             - Stop all containers"
	@echo "  make restart          - Restart all containers"
	@echo "  make status           - Show containers status"
	@echo "  make clean            - Remove project containers and images"
	@echo "  make logs             - Show logs from all containers"
	@echo "  make shell-backend    - Open shell in backend container"
	@echo "  make test             - Run tests"
	@echo "  make ui               - Start ui dev"

install:
	@cd fastapi; python3 -m venv venv; . venv/bin/activate; pip install -r requirements.txt
	@cd ui; npm i
	@echo "HINT! Installed backend dependencies ---> use 'source fastapi/venv/bin/activate' to activate the virtual environment"
	@echo "HINT! Installed ui dependencies ---> use npm into ui dir for more options"

dev:
	@cd fastapi; . venv/bin/activate; python -m app.main
ui:
	@cd ui; npm run dev
run:
	@docker-compose -p $(PROJECT_NAME) up -d --build

build:
	@docker-compose -p $(PROJECT_NAME) build

start:
	@docker-compose -p $(PROJECT_NAME) up -d

stop:
	@docker-compose -p $(PROJECT_NAME) stop

restart: stop start

status:
	@echo "Container Status:"
	@docker ps -a --filter "name=$(PROJECT_NAME)"

clean:
	@echo "Cleaning up project containers and images..."
	@docker-compose -p $(PROJECT_NAME) down --rmi local
	@docker image prune -f

logs:
	@docker-compose -p $(PROJECT_NAME) logs -f


shell-backend:
ifdef BACKEND_ID
	@docker exec -it $(BACKEND_ID) /bin/sh
else
	@echo "Backend container is not running"
endif

test:
	@pytest