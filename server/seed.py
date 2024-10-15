from app import app
from models import db, Group,Post,user_groups,User
from faker import  Faker
from random import choice as rc

fake = Faker()

users = []

def create_user():
    for _ in range(10):
        u = User(
            username=fake.name(),
            email=fake.email()
        )
        users.append (u)
    # return users

def create_post(users):
    posts=[]
    for _ in range(10):
        p = Post(
            title=fake.file_name(),
            description = fake.sentence(),
            user_id= rc([user.id for user in users])
        )
        posts.append(p)
    return posts

def creating_group():
    groups=[]
    for _ in range(5):
        gp = Group(
            name = fake.name()
        )
        groups.append(gp)
        for _ in range(3):
            gp.users.append(rc(users))
    return groups

# def creating_group_users(groups, users):
#     group_users = []
#     for _ in range(5):
#         ug = user_groups(
#             user_id = rc([user.id for user in users]),
#             group_id = rc([group.id for group in groups])
#         )
#         group_users.append(ug)
#     for _ in range(4):
        
#     return group_users

with app.app_context():
    print('Clearing database======')
    Group.query.delete()
    Post.query.delete()
    # user_groups.query.delete()
    User.query.delete()
    db.session.query(user_groups).delete()
    db.session.commit()
    
    print('seeding users=======')
    create_user()
    db.session.add_all(users)
    db.session.commit()
    
    print('Seeding posts')
    posts = create_post(users)
    db.session.add_all(posts)
    db.session.commit()
    
    print('Seeding groups')
    groups = creating_group()
    db.session.add_all(groups)
    db.session.commit()
    
    # print('group_users============')
    # user_groups = creating_group_users(groups, users)
    # db.session.add_all(user_groups)
    # db.session.commit()
    
    print("DONE SEEDING!!!!!!!!!!!!!!!!")
    
    