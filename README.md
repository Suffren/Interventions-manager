# Interventions manager

This application is a prototype allowing to manage interventions. A simple interface allows you to consult, add, modify or delete these interventions.

**Interventions manager** is built with AngularJS 1.7, Python 2.7, Flask 1.1.2 and SQLite3.


### Installation:

First, you need to download this repository or clone it with [Git](https://git-scm.com/downloads) using this command in your favorite command-line interpreter:

`git clone git@github.com:Suffren/Interventions-manager.git`

`cd Interventions-manager/`

Then, you need to install [Node.js](https://nodejs.org/en/download/) and [Python](https://www.python.org/downloads/release/python-2713/) **version 2.7**:

During the Python installation, choose "Will be installed on your local drive" when clicking on "Add python.exe to Path" on the "Customize Python" window.

Install Flask with the Python package installer:

`pip install -U Flask`

Install Flask-cors:

`pip install -U flask-cors`


You're now set to run the server !

`cd api/`

`Python api.py`



Install 'http-server' npm package on **another** command-line window:

`npm install --global http-server`

and run the web server from the "Interventions-manager" directory:

`http-server -a localhost -p 8050`

Finally, in your browser address bar, paste "localhost:8050".