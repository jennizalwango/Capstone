# Capstone

 Capstone is a casting ungency 

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

l would recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
```buildoutcfg
python -m venv (name of your virtual evironment)
```
#### Activate the virtual evirnoment
Its is time to activate your virtual environment run:
```buildoutcfg
source <name of virtual environment>/bin/activate
```


#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies and run:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) 
 
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)


## Running the server

First ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.


### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `get:movies`
    - `post:movies`
    - `patch:movies`
    - `delete:movies`
    - `get:actors`
    - `post:actors`
    - `patch:actors`
    - `delete:actors`
6. Create new roles for:
    - Casting Assistant
        - can `view:actors`
        - can `view:movies`
        
    - Casting Director
        - can perform all actions for the casting assistant
        
            - `get:movies`
            - `post:movies`
            - `patch:movies`
            - `get:actors`
            - `patch:actors`
            - `delete:actors`

    - Executive Producer
        - Can perform all actions for the casting director
        
            - `get:movies`
            - `post:movies`
            - `patch:movies`
            - `delete:movies`
            - `get:actors`
            - `post:actors`
            - `patch:actors`
            - `delete:actors`
