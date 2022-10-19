# Setup up Graphql API

## Run API

### Virtual env:
- Create: `python3 -m venv /path-to-new-virtual-environment`
- Activate: `source /path-to-new-virtual-environment/bin/activate`
- Deactivate: `deactivate`

### Libraries
- Install libraries from requirements.txt file: `pip install -r requirements.txt`
- Update libraries to requirements.txt file: `pip freeze > requirements.txt`

### Run containers:
`do up -d`

### Run flask API. Server will start running on http://127.0.0.1:5000
`python manage.py run`

### Access Graphql API playground
`http://127.0.0.1:5000/graphql`

### Access Rest API playground
`http://127.0.0.1:5000/graphql`

## Manage DB

### Create DB:
`python manage.py create_db`

### Ensure the Post table was created:
1. `dco exec db psql --username=hello_flask --dbname=hello_flask_dev`
2. `# \dt`

### Add test data to DB:
`python manage.py seed_db`

### Select data from DB:
1. `dco exec db psql --username=hello_flask --dbname=hello_flask_dev`
2. `select * from post;`