run:
	flask --app run run --debug
test:
	pytest
coverage:
	coverage run -m pytest
report:
	coverage report
Phony:
	run test coverage report