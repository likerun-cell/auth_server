#!/usr/bin/env bash

# exit on error
set -e

SETTINGS_ROOT=auth_server.settings
# when used in production environment
# migrations should be standalone service so avoid multiple migrate run concurrently breaking the database

# check setting modules
if [[ -z "${DJANGO_SETTINGS_MODULE}" ]]; then
    if [[ -z "${PYTHON_ENV}" ]] ; then
        echo "both DJANGO_SETTING_MODULE and PYTHON_ENV not defined"
        exit 1;
    else
        case ${PYTHON_ENV} in
        "development")
            export DJANGO_SETTINGS_MODULE="${SETTINGS_ROOT}.development"
            ;;
        "production")
            export DJANGO_SETTINGS_MODULE="${SETTINGS_ROOT}.production"
            ;;
        "test")
            export DJANGO_SETTINGS_MODULE="${SETTINGS_ROOT}.test"
            ;;
        *)
            echo "PYTHON_ENV must be one of  development, test, production"
            exit 1
            ;;
        esac
    fi
fi

# check database settings in prod
if [[ "${DJANGO_SETTINGS_MODULE}" == "${SETTINGS_ROOT}.production" ]] ; then
    if [[ -z ${POSTGRES_DB} || -z ${POSTGRES_USER} ]]; then
        echo "POSTGRES_DB POSTGRES_USER must set"
        exit 1
    fi
fi

# check if the database needs to be migrated
if [[ "${DB_MIGRATE}" == "migrate" ]] ; then
    pipenv run python manage.py makemigrations
    pipenv run python manage.py migrate
fi

