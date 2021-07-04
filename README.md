
# Cut and Go: A simple URL shortener

![Demo](https://raw.githubusercontent.com/codegleb/cut_and_go/master/assets/demo.gif)
## Run

docker-compose.yml file setups `PostgreSQL`, `Nginx`, `Django`.
### Add variables in docker-compose.yml
```bash
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_NAME=
DB_USER=
USER_PASSWORD=
DB_HOST=db
DB_PORT=5432
ALLOWED_HOSTS=
SECRET_KEY=
DEBUG=
SITE_URL=
```

### Run `docker-compose up` in the project directory.

**Note**: [install docker](https://docs.docker.com/engine/install/)

## License

Usage is provided under the [MIT License](opensource.org/licenses/mit-license.php). See LICENSE for the full details.
