#!/bin/bash

function POSTGRESQL() {
    systemctl restart postgresql
    echo "----------------- PostgreSQL Starting Finished. -----------------"
    echo "                               "
}
function COLLECTSTATIC() {
    python3 manage.py collectstatic --no-input
    echo "----------------- Flake8 Finished. -----------------"
    echo "                               "
}
function MAKEMIGRATIONS() {
    python3 manage.py makemigrations
    echo "----------------- Makemigrations Models Finished. -----------------"
    echo "                               "
}
function MIGRATE() {
    python3 manage.py migrate
    echo "----------------- Migrated Models Finished. -----------------"
    echo "                               "
}
function RUNSERVER() {
    python3 manage.py runserver 127.0.0.1:7560
    echo "----------------- Server Started Now. -----------------"
}
function STORAK() {
	POSTGRESQL
    MAKEMIGRATIONS
    MIGRATE
    COLLECTSTATIC
    RUNSERVER
}
STORAK