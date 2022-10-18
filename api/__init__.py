from datetime import date

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from api.config import Config
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

app = Flask(__name__)
CORS(app)

config = Config()
app.config.from_object(Config())

db = SQLAlchemy(app)

from api.queries import listPosts_resolver, getPost_resolver
from api.mutations import create_post_resolver, update_post_resolver, delete_post_resolver
from api.models import Post

query = ObjectType("Query")
mutation = ObjectType("Mutation")
query.set_field("listPosts", listPosts_resolver)
query.set_field("getPost", getPost_resolver)
mutation.set_field("createPost", create_post_resolver)
mutation.set_field("updatePost", update_post_resolver)
mutation.set_field("deletePost", delete_post_resolver)

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

@app.route('/posts', methods=["GET"])
def get_all_posts():
    posts = [post.to_dict() for post in Post.query.all()]
    return posts


@app.route('/posts/<id>', methods=["GET"])
def get_post(id):
    post = Post.query.get(id)

    if post is None:
        return {"message": "Post is not found"}, 404

    return post.to_dict()


@app.route('/posts', methods=["POST"])
def create_post():
    data = request.json
    today = date.today()
    post = Post(
        title=data['title'], description=data['description'], created_at=today.strftime("%b-%d-%Y")
    )
    db.session.add(post)
    db.session.commit()

    return post.to_dict(), 201


@app.route('/posts/<id>', methods=["PATCH"])
def patch_post(id):
    data = request.json
    post = Post.query.get(id)

    if post is None:
        return {"message": "Post is not found"}, 404

    if "title" in data:
        post.title = data['title']
    if "description" in data:
        post.description = data['description']
    db.session.add(post)
    db.session.commit()

    return {}, 204


@app.route('/posts/<id>', methods=["DELETE"])
def delete_post(id):
    post = Post.query.get(id)

    if post is None:
        return {"message": "Post is not found"}, 404

    db.session.delete(post)
    db.session.commit()

    return {}, 204


@app.route('/')
def hello():
    return 'Test first endpoint'
