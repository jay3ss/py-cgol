TEST_PATH=./

help:
	@echo "make init"
	@echo "		initialize the project"
	@echo "make init-dev"
	@echo "		intialize the project for development"
	@echo "make clean-pyc"
	@echo "		remove python artifacts"

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force {} +

test: clean-pyc
	py.test --verbose --color=yes $(TEST_PATH)

init:
	python -m pip install --upgrade pip

init-dev:
	make init
	python -m pip install -r dev-requirements.txt
