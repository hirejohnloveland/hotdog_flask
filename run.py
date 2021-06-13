from app import create_app, db
# from app.blueprints.users.models import User
from db_manager import Db_Build, Db_Destroy



app = create_app()

# db_init is the script which initially populates the database with the items


@app.shell_context_processor
def make_shell_context():
    return {'app': create_app, 'db': db, 'db_init': Db_Build.db_init_all, 'db_destroy': Db_Destroy.db_destroy }
