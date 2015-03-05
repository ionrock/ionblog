build:
	xe tinker -b

release:
	rsync -r blog/html/ eric@ionrock.org:htdocs/
