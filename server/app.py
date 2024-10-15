# from flask import Flask
from flask import Flask, make_response
from flask_migrate import Migrate
from flask_restful import Api
from models import *

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


@app.route('/')
def index():
    return '<h1>I am running</h1>'

@app.route('/users')
def getting_users():
    users = [user.to_dict() for user in User.query.all()]
    return  make_response(users, 200)

@app.route('/posts')
def get_posts():
    posts = [post.to_dict() for post in Post.query.all()]
    return make_response(posts, 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)