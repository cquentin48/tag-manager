## Run the unit test suite
test:
	pytest tests/

## HTML Unit test report
test_report:
	pytest --html=unit_test/report.html --self-contained-html

## Generates executable
exec_file:
	pyinstaller --onefile ./cli/main/main.py

## Generates executable silent
exec_file_silent:
	pyinstaller --noconsole --onefile ./cli/main/main.py

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