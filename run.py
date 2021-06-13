from app import create_app, db
# from app.blueprints.users.models import User
from app.blueprints.menu.models import db_init



app = create_app()

# db_init is the script which initially populates the database with the items


@app.shell_context_processor
def make_shell_context():
    return {'app': create_app, 'db': db, 'db_init': db_init }
