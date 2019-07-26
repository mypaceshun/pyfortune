PYTHON3		= python3
VENV		= venv
ACTIVATE	= . ./${VENV}/bin/activate
TARGET		= testpypi

.PHONY: usage
usage:
	@echo "Usage: ${MAKE} TARGET"
	@echo ""
	@echo "Targets:"
	@echo "  build-env      build venv directory"
	@echo "  doc            build document"
	@echo "  test           run test scripts"
	@echo "  test_all       run all test VerySlow!!"
	@echo "  lint           run flake8"
	@echo "  format         run autopep8"
	@echo "  clean          remove venv directory"
	@echo ""
	@echo "  build          build package"
	@echo "  upload         upload to ${TARGET}"
	@echo "    TARGET=pypi  upload to pypi"


.PHONY: build-env
build-env:
	@${MAKE} -s ${VENV}
	@${MAKE} -s secrets

${VENV}: requirements.txt
	${PYTHON3} -m venv ${VENV}
	${ACTIVATE} && pip install --upgrade pip setuptools wheel
	${ACTIVATE} && pip install --upgrade -r requirements.txt -r dev-requirements.txt
	touch ${VENV}

secrets:
	echo "username" > secrets
	echo "password" >> secrets

.PHONY: doc
doc:
	${ACTIVATE} && sphinx-apidoc -f -o docs_build/ pyfortune/
	${ACTIVATE} && cd docs_build/ && make html
	cp -rfv docs_build/_build/html/* docs/

.PHONY: test
test: ${VENV}
	${ACTIVATE} && python -m pytest tests -m "not slow"

.PHONY: test_all
test_all: ${VENV}
	${ACTIVATE} && python -m pytest tests

.PHONY: lint
lint: ${VENV}
	${ACTIVATE} && flake8 --count pyfortune || :

.PHONY: format
format: ${VENV}
	${ACTIVATE} && autopep8 -ir pyfortune

.PHONY: clean
clean:
	rm -rf ${VENV} dist build

.PHONY: build
build: ${VENV}
	rm -rf dist build *.egg-info
	${ACTIVATE} && python setup.py sdist bdist_wheel
	${ACTIVATE} && twine check dist/*

.PHONY: upload
upload:
	${MAKE} build
	${ACTIVATE} && twine upload --repository ${TARGET} dist/*
