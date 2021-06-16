# Cut and Go: A simple URL shortener

![Demo](https://raw.githubusercontent.com/codegleb/cut_and_go/master/assets/demo.gif)

# Run locally

**Note**: Run all commands in the project root directory(the directory that you clone)

### Create virtual environment

```bash
python -m venv env
```

### Activate environment

```bash
source env/bin/activate
```

### Install requirements

```bash
pip install -r requirements.txt
```

### Generate secret kay

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
Copy the output and add it to the environment variable

### Set environment variables

You can create .env file and add the following lines:

```bash
SECRET_KEY="<Secret key (generated at the previous paragraph)>"
SITE_URL="<Site url (for default set 127.0.0.1:8000)>
DEBUG="<True or False>"
ALLOWED_HOSTS="<Allowed hosts (for default set '127.0.0.1')>"
DB_ENGINE="<DB engine>"
DB_NAME="<DB name>"
DB_USER="<DB user with DB access>"
USER_PASSWORD="<DB user password>"
DB_HOST="<DB host>"
DB_PORT="<DB port>"
```
**Note**: `SITE_URL` and `ALLOWED_HOSTS` should be the same, but in `ALLOWED_HOSTS` address without a port

Or you can export variables above manually

```bash
export <VARIABLE_NAME>="<VALUE>"
```

### Migrations

**Note**: `requirements.txt` doesn't contain any DB engine, but it is described in [next chapter](#add-database-support)

```bash
python manage.py makemigration cutter
python manage.py migrate
```

### Run server

```bash
python manage.py runserver
```
**Note**: If you set `SITE_URL` and `ALLOWED_HOSTS` values different from `127.0.0.1:8000` you should add their value at the end of the command ```python manage.py runserver 0.0.0.0:8000```

# Add database support (PostgreSQL as example)

### Install required modules:

```bash
pip install psycopg2
```
### Add engine to environment variable

[Install PostgreSQL](postgresql.org/download/)

```bash
export DB_ENGINE="django.db.backends.postgresql_psycopg2"
```
