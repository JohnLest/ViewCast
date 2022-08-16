# ViewCast
Software for managing information broadcast on televisions

## Description
Mrs. Ramonfosse, who represents our client, asks us to create an application that allows multimedia content to be broadcast on any screen. This in order to be able to display videos, images or documents on televisions which can be located in various places within the premises of a company.

## Installation
As the technology used to develop the website is core technology, it is very easy to put the project into production. If the server is a Microsoft system, you just have to think about installing Python 3.9 which is not native to this OS (available here: https://www.python.org/downloads/).
If you want to put into production via docker services, a docker-compose is available for mariadb and a Dockerfile for the web project.
For Mariadb, just go to the folder that contains the docker-compose and type the following command: `docker-compose -d`. It will create a mariadb container on port 3306 and a phpmayadmin container on port 8081 in order to have a graphical interface. Once mariadb is installed, just import the sql file.
For the project itself, you must first create the image from the provided Dockerfile, so just type the command: `docker build -t viewcast_image .`, then the command `docker run -d -- name boomcraft_api -p 40100:40100 boomcraft_api_image` (of course you can change the ports to your liking).
If you don't want to go through docker, just create a virtual environment with the command `python3 -m ./venv/` (you can of course change the path of the environment) and then launch it with the command `. /venv/Script/Activate`. Once the environment is launched, download all the libraries the project needs with `pip install –no-cache-dir –upgreade -r ./requierments.txt` and to finish launch the project with `python3 -m flask run – host=0.0.0.0 –port=40100`

## License
This project is a MIT License
