install:
	pip install -e . -r requirements-dev.txt

test:
	pytest -q

lint:
	ruff check src tests

format:
	ruff format src tests

quality: lint test

build:
	docker build -t drivevision-yolo .
