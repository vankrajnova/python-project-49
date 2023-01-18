install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl

brain-games:
	poetry run brain-games

.PHONY: install build publish package-install reinstall brain-games
