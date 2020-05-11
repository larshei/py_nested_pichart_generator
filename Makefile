all: setup run

run:
	python3 run.py

setup:
	bash scripts/setupPythonVenvAndPackages.sh

freeze:
	bash scripts/freezeDependencies.sh
