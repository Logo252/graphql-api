from flask.cli import FlaskGroup

from api import app, db, models
from datetime import datetime

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    current_date = datetime.today().date()
    post = models.Post(title="A new morning", description="A new morning details", created_at=current_date)
    db.session.add(post)
    db.session.commit()


if __name__ == "__main__":
    cli()
