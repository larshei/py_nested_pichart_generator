all: setup run

run:
	python3 run.py

setup:
	bash setupPythonVenvAndPackages.sh

freeze:
	bash freezeDependencies.sh
