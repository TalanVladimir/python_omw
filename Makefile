.ONESHELL:
VENV_DIR=.venv
ACTIVATE_VENV:=. $(VENV_DIR)/bin/activate
PIP=pip3

# aplinkos paleidimas

start:
	${ACTIVATE_VENV}

echo:
	echo ${ACTIVATE_VENV}

end:
	deactivate

# aplinkos komandos

env:
	virtualenv -p python3 .venv

install:
	${PIP} install -r requirements.txt

save:
	${PIP} freeze > requirements.txt

# scriptai

xlsx:
	pymon ./src/xlsx/xlsx_script.py -p "*.sql"

parser:
	pymon ./src/parser/custom_parser.py