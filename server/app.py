# from flask import Flask
from flask import Flask, make_response, request
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

@app.route('/users', methods=['GET','POST'])
def users():
    if request.method == "GET":
        users = [user.to_dict() for user in User.query.all()]
        return  make_response(users, 200)
    elif request.method== 'POST':
        data = request.get_json()
        user = User(
            username=data['username'],
            email=data['email']
        )
        db.session.add(user)
        db.session.commit()
        
        return make_response(user.to_dict(), 204)
@app.route('/users/<int:id>', methods=['DELETE', 'PATCH', 'GET'])
def users_by_id(id):
    if request.method == "GET":
        user = User.query.filter(User.id==id).first()
        return (user.to_dict(),200)
    # elif request.method == "POST":
        

@app.route('/posts', methods=['GET','POST'])
def get_posts():
    posts = [post.to_dict() for post in Post.query.all()]
    return make_response(posts, 200)



if __name__ == '__main__':
    app.run(port=5555, debug=True)