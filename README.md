# Task Description

We want to set up a server to run & serve a `Django` application which uses `Celery` for its
background jobs.

The application source code we want to serve is located in this repo. Please refer to the
[About this repo](#about-this-repo) section for more information.

What you should deliver is a private ansible repository that you added `amirali` and `sazary` users as collaborators.

If you have any questions or find any part of the task vague, don’t hesitate to get in touch with
us.

## Must have requirements:

- The `Django` application should be running and serving views.
- At least one `Celery` worker should be running.
- A suitable broker for `Celery` should be selected. We recommend using `Redis`. Whatever you
  choose for it, security considerations (authentication, authorization, …) should be met.
- A suitable database should be used. We recommend `Postgresql`. Whatever you choose for it,
  security considerations (authentication, authorization, …) should be met.
- All of these modules should be running using `systemd`, `Docker` or any other solution you choose.
  Everything needed for installation & configuration of that solution must be provided in the final
  result.
- Security considerations of the server itself should be met, as we’re going to expose this machine
  to the internet.

## Nice to have requirements:

- Having the application served behind a reverse proxy. We recommend `Nginx`.
- Having a valid SSL certificate for views. The SSL/TLS connection should be terminated in the
  reverse proxy.
- Having the server, application & any of the important components monitored. We recommend using
  `Prometheus` for monitoring.

## Expected result

We don’t want to do any manual config on the server and will use `Ansible` for provisioning the
server from a raw `Ubuntu 22.04` installation. So, the final result we’re expecting from you is a
repo with `Ansible` roles & playbook to do everything.

# About this repo

This application does one simple thing: It will queue some tasks, each of which would just `sleep`
for a duration that is given to it, and displays the results.

## Setting up the project

Install all requirments. Please note that if you've decided to use some other database or broker
from our recommendations, you may have to update the `requirements.txt` file accordingly.

```sh
$ pip install -r requirements.txt
```

Then ask the `manage.py` script to create tables. Please check the `DATABASES` section of the
settings file for default values.

```sh
$ ./manage.py migrate
```

## Running the project

To run the application (HTTP views):

```sh
$ gunicorn core.wsgi:application
```

To run the `celery` workers:

```sh
$ celery -A core worker
```

## Using the project

To trigger a new task:

```sh
$ curl -F duration=45 http://181.41.194.182:3000/tasks/
```

To check the status:

```sh
$ watch -n 2 curl http://181.41.194.182:3000/tasks/<task_id>/
```
