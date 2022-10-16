# Setup up Graphql API

### Active virtual env:
`source venv/bin/active`

### Deactivate virtual env:
`deactivate`

### Run containers:
`do up -d`

### Check containers:
`dco ps`

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