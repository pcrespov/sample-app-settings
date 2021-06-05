

.venv:
	python3 -m pip install -U pip setuptools wheel
	python3 -m pip install -m venv .venv
	# now set source .venv/bin/activate

install:
	.venv/bin/python -m  install -r requirements.txt

	