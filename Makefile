# scriptų komandos

xlsx: # paleidimas pymon
	pymon ./src/xlsx/xlsx_script.py -p "*.sql"

parser: # paleidimas parserio
	pymon ./src/parser/custom_parser.py


# aplinkos komandos

env-install: # venv instaliavimas
	virtualenv -p python3 .venv

env-run:
	. ./.venv/bin/activate

dev-install: # packages instaliavimasa
	pip3 install -r requirements.txt

dev-save: # packages saugojimas į failą
	pip3 freeze > requirements.txt