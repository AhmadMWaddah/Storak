#!/bin/bash

function POSTGRESQL() {
	systemctl restart postgresql
	echo "                                                                                                                            "
	echo "--------------------------------------------------------------------------------------------------		PostgreSQL Starting Finished."
	echo "                                                                                                                            "
}
function COLLECTSTATIC() {
	python3 manage.py collectstatic --no-input
	echo "                                                                                                                            "
	echo "--------------------------------------------------------------------------------------------------		Collect Static Finished."
	echo "                                                                                                                            "
}
function MAKEMIGRATIONS() {
	python3 manage.py makemigrations
	echo "                                                                                                                            "
	echo "--------------------------------------------------------------------------------------------------		Makemigrations Models Finished."
	echo "                                                                                                                            "
}
function MIGRATE() {
	python3 manage.py migrate
	echo "                                                                                                                            "
	echo "--------------------------------------------------------------------------------------------------		Migrated Models Finished.	"
	echo "                                                                                                                            "
}
function RUNSERVER() {
	python3 manage.py runserver 127.0.0.1:7560
	echo "                                                                                                                            "
	echo "--------------------------------------------------------------------------------------------------		Server Started Now."
}
function STORAK() {
	POSTGRESQL
	MAKEMIGRATIONS
	MIGRATE
	COLLECTSTATIC
	RUNSERVER
}
STORAK