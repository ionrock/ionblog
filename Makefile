VENV := .venv


bootstrap:
	virtualenv $(VENV)
	$(VENV)/bin/pip install tinkerer

build:
	tinker -b

release:
	rsync -r blog/html/ eric@ionrock.org:htdocs/
