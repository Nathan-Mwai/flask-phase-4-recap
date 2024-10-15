from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///recap.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.json.compact=False

# metadata= MetaData(naming_convention={
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# })



migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)
