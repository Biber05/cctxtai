ifneq (,$(wildcard .env))
    include .env
    export
endif

run_test:
	python -m cctxtai.runner "/Users/philipp/git/cctxtai/data/00_raw/multiple.json"

run:
	python -m cctxtai.runner "/Users/philipp/git/cctxtai/data/00_raw/2019-02-19_oldp_cases.json" 100