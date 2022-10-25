from datetime import date
from api import db
from api.models import Author


def create_author_resolver(obj, info, name):
    try:
        today = date.today()
        author = Author(
            name=name, created_at=today.strftime("%b-%d-%Y")
        )
        db.session.add(author)
        db.session.commit()
        payload = {
            "success": True,
            "author": author.to_dict()
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }
    return payload


def update_author_resolver(obj, info, id, name):
    try:
        author = Author.query.get(id)
        if author:
            author.name = name
        db.session.add(author)
        db.session.commit()
        payload = {
            "success": True,
            "author": author.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload


def delete_author_resolver(obj, info, id):
    try:
        author = Author.query.get(id)
        db.session.delete(author)
        db.session.commit()
        payload = {"success": True, "author": author.to_dict()}
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload
