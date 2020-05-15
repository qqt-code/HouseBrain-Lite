from flask import Blueprint

from App.ext import db
from App.models import User

blue=Blueprint('first',__name__)

@blue.route('/')
def hello_world():
    return 'Hello World!'
@blue.route('/adduser/')
def add_user():
    # 添加单个数据
    user = User()

    user.u_name = '老贾'
    user.u_age = 18

    db.session.add(user)
    db.session.commit()

    return '数据添加成功'