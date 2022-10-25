from api import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.Date)

    # TO DO: Finish implementing book entity
    # books = db.relationship('Book', backref='book')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": str(self.created_at.strftime('%Y-%m-%d'))
        }
