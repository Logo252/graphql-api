# Setup up Graphql API

## GraphQL vs REST API

### Virtual env:
- Create: `python3 -m venv /path-to-new-virtual-environment`
- Activate: `source /path-to-new-virtual-environment/bin/activate`
- Deactivate: `deactivate`

### Libraries
- Install libraries from requirements.txt file: `pip install -r requirements.txt`
- Update libraries to requirements.txt file: `pip freeze > requirements.txt`

### Run containers:
`docker-compose up -d`

### Change flask env variables to your needs if it is necessary
File name - `.flaskenv`

### Run flask API. Server will start running on http://127.0.0.1:3000
`python manage.py run`

### Access Graphql API playground
`http://127.0.0.1:3000/graphql`

## Manage DB

### Create DB:
`python manage.py create_db`

### Ensure the table created:
1. Access PostgreSQL DB: `dco exec db psql --username=hello_flask --dbname=hello_flask_dev`
2. List of relations: `# \dt`

### Add test data to DB:
`python manage.py seed_db`

### Select data from DB:
1. `dco exec db psql --username=hello_flask --dbname=hello_flask_dev`
2. `select * from table;`

### TO DO:
- Add new entity: Book. Add relation to this entity with author.
- Update API to be able to Create/Get/Update/Delete book by author.
- Update GraphQL to be query/mutate books.
