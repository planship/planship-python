.PHONY: install-dev
install-dev:
	-python3 -m pip install -e planship_openapi_gen
	-python3 -m pip install -e planship

.PHONY: isort
isort:  ## Run isort on the package.
	-isort --check-only planship

.PHONY: mypy
mypy:  ## Run mypy on the package.
	-mypy planship

.PHONY: black
black:  ## Run black on the package.
	-black planship --check

.PHONY: isort-autofix
isort-autofix:  ## Run isort on the package.
	-isort planship

.PHONY: black-autofix
black-autofix:  ## Run black on the package.
	-black planship

.PHONY: flake8
flake8:  ## Run flake8 on the package.
	-flake8 planship --exclude=models.py

.PHONY: autoflake
autoflake:  ## Run flake8 on the package.
	-autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place planship --exclude=__init__.py,models.py

.PHONY: lint
lint: mypy black isort flake8

.PHONY: format
format: autoflake black-autofix isort-autofix