install:
	poetry install
	
brain-games:
	poetry run brain-games
	
build:
	poetry build
	
publish:
	poetry publish --dry-run
	
package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl
	
lint:
	poetry run flake8 brain_games
	
test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

.PHONY: install test lint selfcheck check build
