## Run the unit test suite
test:
	python -m unittest

## Create coverage data
coverage_gen:
	coverage run --omit=cli/**/__init__.py --source=cli -m unittest

## Generates a shell report
coverage_shell:
	coverage report

## Execute the linter
lint:
	pylint cli/ tests/

## Install the dependencies from the requirements.txt file
install:
	pip install -r requirements.txt