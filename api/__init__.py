from datetime import date

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.config import Config
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

app = Flask(__name__)

config = Config()
app.config.from_object(Config())

db = SQLAlchemy(app)

from api.queries import list_authors_resolver, get_author_resolver
from api.mutations import create_author_resolver, update_author_resolver, delete_author_resolver
from api.models import Author

query = ObjectType("Query")
mutation = ObjectType("Mutation")
query.set_field("listAuthors", list_authors_resolver)
query.set_field("getAuthor", get_author_resolver)
mutation.set_field("createAuthor", create_author_resolver)
mutation.set_field("updateAuthor", update_author_resolver)
mutation.set_field("deleteAuthor", delete_author_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


# Graphql routes

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code


# API routes

@app.route('/authors', methods=["GET"])
def get_all_authors():
    authors = [author.to_dict() for author in Author.query.all()]
    return authors


@app.route('/authors/<id>', methods=["GET"])
def get_author(id):
    author = Author.query.get(id)

    if author is None:
        return {"message": "Author is not found"}, 404

    return author.to_dict()


@app.route('/authors', methods=["POST"])
def create_author():
    data = request.json
    today = date.today()
    author = Author(
        name=data['name'], created_at=today.strftime("%b-%d-%Y")
    )
    db.session.add(author)
    db.session.commit()

    return author.to_dict(), 201


@app.route('/authors/<id>', methods=["PATCH"])
def patch_author(id):
    data = request.json
    author = Author.query.get(id)

    if author is None:
        return {"message": "Author is not found"}, 404

    if "name" in data:
        author.name = data['name']
    db.session.add(author)
    db.session.commit()

    return {}, 204


@app.route('/authors/<id>', methods=["DELETE"])
def delete_author(id):
    author = Author.query.get(id)

    if author is None:
        return {"message": "Author is not found"}, 404

    db.session.delete(author)
    db.session.commit()

    return {}, 204


@app.route('/')
def hello():
    return 'Test first endpoint'
