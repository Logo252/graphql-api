from .models import Author


def list_authors_resolver(obj, info):
    try:
        authors = [author.to_dict() for author in Author.query.all()]
        payload = {
            "success": True,
            "authors": authors
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


def get_author_resolver(obj, info, id):
    try:
        author = Author.query.get(id)
        payload = {
            "success": True,
            "author": author.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Author item matching {id} not found"]
        }
    return payload
