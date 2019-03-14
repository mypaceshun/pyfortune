PYTHON3		= python3
VENV		= venv
ACTIVATE	= . ./${VENV}/bin/activate

.PHONY: usage
usage:
	@echo "Usage: ${MAKE} TARGET"
	@echo ""
	@echo "Targets:"
	@echo "  build-env      build venv directory"
	@echo "  doc            build document"
	@echo "  test           run test scripts"
	@echo "  test_all       run all test VerySlow!!"
	@echo "  clean          remove venv directory"


.PHONY: build-env
build-env:
	${MAKE} ${VENV}
	${MAKE} secrets

${VENV}: requirements.txt
	${PYTHON3} -m venv ${VENV}
	${ACTIVATE} && pip install --upgrade pip setuptools wheel
	${ACTIVATE} && pip install --upgrade -r requirements.txt -r dev-requirements.txt

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

.PHONY: clean
clean:
	rm -rf ${VENV}
