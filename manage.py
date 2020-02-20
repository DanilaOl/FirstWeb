import json
from model import Base, add_user
from flask.cli import FlaskGroup
from app import app

cli = FlaskGroup(app)


@cli.command('reset_db')
def reset_db():
    Base.metadata.drop_all()
    Base.metadata.create_all()


@cli.command('fill_db')
def fill_db():
    with open('MOCK_DATA.json') as f:
        mock = json.load(f)
    for i in mock:
        add_user(**i)


cli()
# reset_db()
# fill_db()
