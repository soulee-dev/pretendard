.PHONY: help build test clean

help:
	@echo "###"
	@echo "# Build targets for Pretendard families"
	@echo "###"
	@echo
	@echo "  make build:  Builds the fonts and places them in the fonts/ directory"
	@echo "  make test:   Runs fontbakery (Google Fonts profile) on the built fonts"
	@echo "  make clean:  Removes the virtual environment and build stamp"
	@echo
	@echo "Note: Pretendard Std is derived from Pretendard via"
	@echo "scripts/refine/create-std.py and is not built by this Makefile."
	@echo

build: build.stamp

venv: venv/touchfile

build.stamp: venv $(wildcard sources/config*.yaml)
	rm -rf fonts
	(for config in sources/config*.yaml; do . venv/bin/activate; gftools builder $$config || exit 1; done) && touch build.stamp

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

test: build.stamp
	. venv/bin/activate; fontbakery check-googlefonts $$(find fonts -type f -name "*.ttf")

clean:
	rm -rf venv build.stamp
