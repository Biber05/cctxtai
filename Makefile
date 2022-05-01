ifneq (,$(wildcard .env))
    include .env
    export
endif

run_test:
	python -m cctxtai.preprocessing.runner "/Users/philipp/git/cctxtai/data/00_raw/multiple.json"

run:
	python -m cctxtai.preprocessing.runner "/Users/philipp/git/cctxtai/data/00_raw/2019-02-19_oldp_cases.json" 100

search_legal:
	python -m cctxtai.search "openlegal" "Ablehnung Prozesskostenhilfe"

search_hp:
	python -m cctxtai.search "harry_potter" "Dumbledore Dead" 10