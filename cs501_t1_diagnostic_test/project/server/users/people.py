from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

users = Blueprint('users', __name__)

class UsersAPI(MethodView):
    def get(self):
        userList = [user for user in User.query]

        emailList = ", "
        emails = [user.email for user in userList]
        emailList = emailList.join(emails)
        return "[" + emailList + "]"



users_view = UsersAPI.as_view('Users_API')

users.add_url_rule(
    '/users/index',     
    view_func=users_view,
    methods=['GET']
)