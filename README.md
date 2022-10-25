## Setup up Graphql API

### Virtual env:
- Create: `python3 -m venv /path-to-new-virtual-environment`
- Activate: `source /path-to-new-virtual-environment/bin/activate`
- Deactivate: `deactivate`

### Libraries
- Install libraries from requirements.txt file: `pip install -r requirements.txt`
- Update libraries to requirements.txt file: `pip freeze > requirements.txt`

### Run containers:
`docker-compose up -d`

### Change flask env variables to your needs
File name - `.flaskenv`

### Run flask API. Server will start running on http://127.0.0.1:3000
`python manage.py run`

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

## REST API
- GET list of authors: /authors
- GET one author: /authors/:id
- CREATE new author: /authors
- PATCH update author: /authors/:id
- DELETE delete author: /authors/:id

## GraphQL API playground

### Access GraphQL API playground
`http://127.0.0.1:3000/graphql`

### Example queries 
Get author:
```
query GetAuthor {
  getAuthor(id: "2") {
    author {
      id
      name
    }
    success
    errors
  }
}
```

Get all authors:
```
query AllAuthors {
  listAuthors {
    authors {
      id,
      name
    }
    success
    errors
  }
}
```

### Example mutations 
Create new author:
```
mutation CreateNewAuthor {
  createAuthor(name: "Jonas") {
    author {
      id
      name
      created_at
    }
    success
    errors
  }
}
}
```

Update author:
```
mutation UpdateAuthor {
  updateAuthor(id: "3", name: "Ciurka") {
    success
    errors
  }
}
```

Delete author:
```
mutation DeleteAuthor {
  deleteAuthor(id:"5") {
    author {
      id
      name
      created_at
    }
    success
    errors
  }
}
```

### TO DO:
1. Add new entity: Book with title and category. Add relation to this entity with author: One to Many.
Update seed_db command (manage.py) accordingly to add multiple books to author.
2. Update API to be able to Create/Get/Update/Delete book by author.
3. Update GraphQL to query/mutate books.
