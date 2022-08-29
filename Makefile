VENV_PATH='venv/bin/activate'
ENVIRONMENT_VARIABLE_FILE='.venv'

define find.functions
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
endef

help: ## вывод доступных команд
	@echo 'The following commands can be used.'
	@echo ''
	$(call find.functions)

setup: ## установка и активация виртуального окружения. установка/обновление pip и установка зависимостей
setup:
	python3 -m venv venv
	source $(VENV_PATH)
	source $(ENVIRONMENT_VARIABLE_FILE)
	python3 -m pip install --upgrade pip
	pip install -r requirements.txt

leave: ## очистка и деактивация виртуального окружения
leave: clean
	deactivate

clean: ## очистка кэша
clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
