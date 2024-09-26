BIN=.venv/bin/

# aplinkos paleidimas

start:
	. $(BIN)activate

end:
	deactivate

# aplinkos komandos

env-install: # venv instaliavimas
	virtualenv -p python3 .venv

dev-install: # packages instaliavimasa
	pip3 install -r requirements.txt

dev-save: # packages saugojimas į failą
	pip3 freeze > requirements.txt

# scriptai

xlsx: # paleidimas pymon
	pymon ./src/xlsx/xlsx_script.py -p "*.sql"

parser: # paleidimas parserio
	pymon ./src/parser/custom_parser.py
