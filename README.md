## cornershop-backend-test

### Running the development environment

* `make up`

Inside the container, you have several options, to see them go to `.docker/dev` directory
you can run that commands in the `entrypoint` of the container, we recommend see too the `docker-entrypoint.sh`

> Run the migrations in the database with `dev migrate`, the migrations needed are in the 
> project.

##### Rebuilding the base Docker image

* `make rebuild`

##### Resetting the local database

* `make reset`

### Hostnames for accessing the service directly

* Local: http://127.0.0.1:8000 or http://localhost:8000


### Slack notification

The app has a task in charge of send a slack notification.
Ensure You have the `SLACK_PATH_PUSH_NOTIFICATION_CH` in a `.env` file without the 
hook notification path `https://hooks.slack.com/services/` it is in the settings. Put the `.env` file
in the same directory of the `docker-compose.yaml` file.

For its configuration see the [documentation](https://api.slack.com/messaging/webhooks#incoming_webhooks_programmatic).


### Create super user
You need a superuser to use all the functionality:
* Create menus.
* Create meals
* See all the day requests.
* List all the menus and their ids.

For that you need a email and password, and in the console,
run `make up` afther that `python manage.py createsuperuser`,
and configure his credentials, and it is all.

> If you want to send the notifications, change the docker-compose file, in specific
> the service backend without a `command` and type `docker-compose up`:
> ```yaml
> services:
>  backend: &backend
>    build:
>      context: .
>      dockerfile: .docker/Dockerfile_base
>  #  command: shell
> ```