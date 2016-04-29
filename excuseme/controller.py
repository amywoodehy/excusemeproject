from flask import Blueprint, jsonify, request, abort, url_for, redirect
from flask import current_app as app
from excuseme.models import Excuse, User

api = Blueprint('api', __name__)


@api.route('/list')
def get_list():
    app.logger.warning("what the fucking fuck?")
    return jsonify([])


@api.route('/add')
def add_excuse():
    pass


@api.route('/random')
def get_random():
    rnd = Excuse.objects.first()
    app.logger.debug(rnd)
    return jsonify([])


@api.route('/user/<username>')
def profile(username):
    user = User.objects.first_or_404(username=username)
    print(user)
    return jsonify({})


@api.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    name = request.json.get('name')
    if not username or not password:
        abort(400)
    if User.objects(username=username).first() or User.objects(email=email).firts:
        abort(400)
    user = User(username=username, email=email, password=password)
    user.save()
    return redirect(url_for('.profile', username=username))
