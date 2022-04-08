from flask import Blueprint, render_template, jsonify, request, send_from_directory,flash, redirect, url_for
from flask_jwt import jwt_required
from flask_login import LoginManager, current_user, login_user, login_required, login_manager



from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
)
from App.controllers import *

user_views = Blueprint('user_views', __name__, template_folder='../templates')




@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/api/users')
def client_app():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')

@user_views.route('/game')
@login_required
def render_game():
    return render_template('index.html')

@user_views.route('/signup', methods=['POST'])
def signup_user():
    data = request.form
    stat = create_user(data['username'], data['email'], data['password'])
    if(stat == 'pass'):
        flash('Acount Created!')
        return render_template('login.html')
    else:
        flash('Username or Email already in use!')
        return render_template('signup.html')
    
@user_views.route('/auth',methods=['POST'])
def logsIn_user():
    data = request.form
    user = authenticate(data['username'], data['password'])
    if user == None:
        flash('Wrong Username or Password!')
        return render_template('login.html')
    login_user(user)
    #return redirect(url_for('user_views.render_game'))
    return render_game()

@user_views.route('/logout', methods=['GET'])
@login_required
def logout():
  logout_user()
  flash('Logged Out!')
  return render_template('login.html')