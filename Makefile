PYTHON3		= python3
VENV		= venv
ACTIVATE	= . ./${VENV}/bin/activate

.PHONY: usage
usage:
	@echo "Usage: ${MAKE} TARGET"
	@echo ""
	@echo "Targets:"
	@echo "  build-env      build venv directory"
	@echo "  test           run test scripts"
	@echo "  clean          remove venv directory"


.PHONY: build-env
build-env:
	${MAKE} ${VENV}

${VENV}: requirements.txt
	${PYTHON3} -m venv ${VENV}
	${ACTIVATE} && pip install --upgrade pip setuptools wheel
	${ACTIVATE} && pip install --upgrade -r requirements.txt -r dev-requirements.txt

.PHONY: test
test:
	${ACTIVATE} && python -m pytest tests

.PHONY: clean
clean:
	rm -rf ${VENV}
