

.PHONY: devenv
devenv: .env
	python3 -m venv .venv
	.venv/bin/pip install -U pip
	.venv/bin/pip install -r requirements.txt
	# now set source .venv/bin/activate


.env: .env-sample
	cp $< $@



.PHONY: demo
demo: .env ## A demo for the impatient
	python app --help

	#
	# Resolves settings and print an envfile --------------
	#
	python app settings --verbose

	#
	# Now compact -----------------------------------------
	#
	python app settings --verbose --compact


	#
	# Now json --------------------------------------------
	#
	python app settings --as-json