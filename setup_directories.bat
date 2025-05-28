@echo off
echo Creating project directories...

mkdir backend
mkdir backend\moms_project
mkdir backend\apps
mkdir backend\static
mkdir backend\media
mkdir backend\templates

mkdir frontend
mkdir frontend\public
mkdir frontend\src
mkdir frontend\src\assets
mkdir frontend\src\components
mkdir frontend\src\views
mkdir frontend\src\router
mkdir frontend\src\store

mkdir deployment
mkdir deployment\docker
mkdir deployment\aws
mkdir deployment\aws\cloudformation
mkdir deployment\aws\scripts

mkdir .github
mkdir .github\workflows

echo Project structure created successfully!