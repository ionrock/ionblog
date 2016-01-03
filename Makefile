VENV := .venv


bootstrap:
	virtualenv $(VENV)
	$(VENV)/bin/pip install tinkerer

build:
	$(VENV)/bin/tinker -b

release:
	rsync -r blog/html/ eric@ionrock.org:htdocs/
