unittest:
	py.test --junitxml=test-output/unit-test-output.xml --cov-report=html:test-output/unit-test-cov-report

run:
	python3 manage.py runserver
