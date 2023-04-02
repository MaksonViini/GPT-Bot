# USAGE: make <command>
# Example: make add_dev_reqs
# It will create a archive with all libs
.PHONY: install format lint test sec clean cover add_dev_reqs before_push_code

# Terminal Colors
Color_Off=\033[0m
Black=\033[1;30m
Red=\033[1;31m
Green=\033[1;32m
Yellow=\033[1;33m

pip_install_basic:
	pip install fastapi black isort pipreqs uvicorn

add_dev_reqs:
	pip freeze > dev-requirements.txt

install:
	@python venv/bin/activate_this.py
	@pip install -r dev-requirements.txt

format:
	@isort .
	@black .

lint:
	@isort . --check

req:
	@pipreqs . --force

doc:
	@pydocstyle omie_faturamento/*.py

security:
	@pip-audit

clean:
	find . -type d -name __pycache__ -exec rm -r {} \+

run_app:
	uvicorn src.main:app --reload

before_push_code:
	@python venv/bin/activate_this.py
	${MAKE} add_dev_reqs
	${MAKE} clean
	${MAKE} format