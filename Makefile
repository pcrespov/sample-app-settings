

.PHONY: devenv
devenv: .env
	python3 -m venv .venv
	.venv/bin/pip install -U pip
	.venv/bin/pip install -r requirements.txt
	# now set source .venv/bin/activate


.env: .env-sample-1
	cp $< $@
