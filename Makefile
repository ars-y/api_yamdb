VENV_PATH='venv/bin/activate'
ENVIRONMENT_VARIABLE_FILE='.venv'
MANAGE_PATH='./api_yamdb'
LOAD_DATA_PATH='./api_yamdb/reviews/management/commands'

define find.functions
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
endef

help: ## вывод доступных команд
	@echo 'The following commands can be used.'
	@echo ''
	$(call find.functions)

setup: ## выполнить команды venv install init run
setup: venv install init run

venv: ## установка и активация виртуального окружения
venv:
	python3 -m venv venv
	source $(VENV_PATH)
	source $(ENVIRONMENT_VARIABLE_FILE)

install: ## установка/обновление pip
install:
	python3 -m pip install --upgrade pip

init: ## установка зависимостей из requirements.txt
init:
	pip install -r requirements.txt

run: ## выполнить миграции и запустить сервер
run:
	cd $(MANAGE_PATH); python3 manage.py migrate
	cd $(MANAGE_PATH); python3 manage.py runserver

load: ## загрузка данных из csv файлов в БД
load:
	cd $(MANAGE_PATH); python manage.py load_users_data
	cd $(MANAGE_PATH); python manage.py load_category_data
	cd $(MANAGE_PATH); python manage.py load_genre_data
	cd $(MANAGE_PATH); python manage.py load_title_data
	cd $(MANAGE_PATH); python manage.py load_genre_title_data
	cd $(MANAGE_PATH); python manage.py load_review_data
	cd $(MANAGE_PATH); python manage.py load_comments_data

leave: ## очистка и деактивация виртуального окружения
leave: clean
	deactivate

clean: ## очистка кэша
clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
