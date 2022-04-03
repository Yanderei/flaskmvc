from flask import Blueprint, redirect, render_template, request, send_from_directory

api_views = Blueprint('api_views', __name__, template_folder='../templates')

@api_views.route('/', methods=['GET'])
def get_api_docs():
    return render_template('login.html')

@api_views.route('/signup', methods=['GET'])
def get__signup_page():
    return render_template('signup.html')