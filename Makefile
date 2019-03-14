PYTHON3		= python3
VENV		= venv
ACTIVATE	= . ./${VENV}/bin/activate
WORKDIR		= _tmp

.PHONY: usage
usage:
	@echo "Usage: ${MAKE} TARGET"
	@echo ""
	@echo "Targets:"
	@echo "  build-env      build venv directory"
	@echo "  doc            build document"
	@echo "  test           run test scripts"
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
	mkdir -p ${WORKDIR}/
	${ACTIVATE} && sphinx-apidoc -F -o ${WORKDIR}/ pyfortune/
	${ACTIVATE} && cd ${WORKDIR}/ && make html
	mv ${WORKDIR}/_build/html/* docs/
	rm -rf ${WORKDIR}

.PHONY: test
test: ${VENV}
	${ACTIVATE} && python -m pytest tests

.PHONY: clean
clean:
	rm -rf ${VENV}
