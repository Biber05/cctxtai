ifneq (,$(wildcard .env))
    include .env
    export
endif

run_test:
	python -m cctxtai.runner "/Users/philipp/git/cctxtai/data/00_raw/test.json"