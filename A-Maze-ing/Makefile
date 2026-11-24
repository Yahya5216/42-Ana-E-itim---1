PYTHON ?= python3
CONFIG ?= config.txt

.PHONY: install run debug clean lint lint-strict package

install:
	$(PYTHON) -m pip install -r requirements.txt

run:
	$(PYTHON) a_maze_ing.py $(CONFIG)

debug:
	$(PYTHON) -m pdb a_maze_ing.py $(CONFIG)

clean:
	$(PYTHON) -c "from pathlib import Path; import shutil; names = {'__pycache__', '.mypy_cache', '.pytest_cache'}; paths = [p for p in Path('.').rglob('*') if p.is_dir() and p.name in names and '.venv' not in p.parts]; [shutil.rmtree(p) for p in sorted(paths, key=lambda p: len(p.parts), reverse=True) if p.exists()]"

lint:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy . --strict

package:
	$(PYTHON) -m build
	$(PYTHON) -c "from pathlib import Path; import shutil; [shutil.copy2(p, Path('.') / p.name) for p in Path('dist').glob('mazegen-*') if p.suffix == '.whl' or p.name.endswith('.tar.gz')]"
