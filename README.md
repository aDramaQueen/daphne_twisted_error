# daphne_twisted_error
Project for testing daphne behind NGINX as proxy server, for error hunting as described in [**Daphne Issue #535: Twisted 24.10.0 incompatibility**](https://github.com/django/daphne/issues/535).

## Requirements

Docker Compose v2.22 or newer, if you want to use the "watch" mode  
(@see **https://docs.docker.com/compose/how-tos/file-watch/**)

If not, then almost every other docker compose versions works

## Usage

- Open your terminal/console and change into project directory
- Run as plain docker composition
  ```shell
  docker compose up
  ```
  *NOTE: Docker compose does NOT look out for changes. Therefore, you have to delete the built image by hand and rebuild the image, to take any changes in considerations! To automate this use the "watch" mode!*

- Run as docker composition with watch mode on (requires Compose v2.22+)
  ```shell
  docker compose watch
  ```
  
- This project implements the standard [**channels tutorial**](https://channels.readthedocs.io/en/latest/tutorial/index.html), therefore open your browser of choice and navigate to:
  ```
  http://localhost:8000/chat
  ```

### Change from UNIX socket to HTTP or vice versa

Go to [**nginx.conf**](resources/nginx.conf) file and change following lines:
  - Line 159 - 163: Uncomment **HTTP** or **UNIX** socket
  - Line 190 - 194: Uncomment **HTTP** or **UNIX** socket

After this is done, go to the [**run-daphne.py**](run-daphne.py) file and change to UNIX socket or HTTP accordingly

## Logging

All access/error logs from the NGINX image are mapped to the [**logs-nginx**](logs-nginx) directory

All access/error logs from the Daphne image are mapped to the [**logs-daphne**](logs-daphne) directory

## Project Preparations (Optional)

*These preparations are only necessary if you want to run this project on your machine, NOT as docker image/composition!!!*

- Open shell/terminal in project directory
- Create virtual environment
    ```shell
    python -m venv .venv
    ```
- Change into venv depending on your shell: (https://docs.python.org/3/library/venv.html#how-venvs-work)
- Install requirements
    ```shell
    pip install -r requirements.txt
    ```
- Make migrations
    ```shell
    python manage.py makemigrations
    ```
- Push migrations to the DB
    ```shell
    python manage.py migrate
    ```
