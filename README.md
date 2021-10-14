# Shared Doc Store
A REST API to simulate a file storage system, with ability filter by topics.

## Description
The Shared Doc Store:
1) Allows GET requests to retreive all Topics, Documents, and Folders.
2) Allows POST requests to create Topics, Documents, and Folders.
3) Allows DELETE requests to remove Topics, Documents, and Folders.
4) Allows PUT requests to update Topics, Documents, and Folders.
5) Ability to retrieve Documents by Topic or by Topic and Folder.

## Getting Started
### Dependencies
I use the following technologies:
* Windows Substem for Linux (WSL2)
    - running Ubuntu 20.04
* pipenv, version 2021.5.29
* python3, version 3.9.7

### Installing
* start and activate a new python environment
    - pipenv shell
* install dependencies
    - pipenv install
* create an .env file in the 'shared_doc_store' main project folder (along side the settings.py file)
    - *the application will not work without the environment variables!*
    - credentials will be sent via email

### Executing program
* when starting the project for the first time, execute SQL commands by making then runnning migrations:
    - ``` python3 manage.py makemigrations ```
    - ``` python3 manage.py migrate ```
* to start server:
    -``` python3 manage.py runserver ```
* to run linter (optional):
    - ``` python3 -m flake8 ```


## Authors
Debra Sparr
[Email](dsparr1010@gmail.com)

## Version History
* 0.1
    * Initial Release

## Acknowledgments
* [Django Web Framework](https://www.djangoproject.com/)
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [All contributors of all open source projects that make coding accessible to everyone](https://quotefancy.com/media/wallpaper/3840x2160/6964-Isaac-Newton-Quote-If-I-have-seen-further-it-is-by-standing-on-the.jpg)
