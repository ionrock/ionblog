VENV=.venv
SERVE_PORT=8080


$(VENV)/bin/tinker:
	virtualenv $(VENV)
	$(VENV)/bin/pip install tinkerer

build: $(VENV)/bin/tinker
	. $(VENV)/bin/activate && $(VENV)/bin/tinker -b

release:
	rsync -r blog/html/ eric@ionrock.org:htdocs/

serve:
	docker run -v `pwd`/blog/html:/usr/share/nginx/html:ro -p $(SERVE_PORT):80 -d nginx
