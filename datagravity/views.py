from flask import request, render_template, jsonify

from . import app, db, redis_db, socketio
from .tasks import get_github_followers


@app.route('/', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/refresh/github/', methods=['GET'])
def refresh_github():
    get_github_followers.apply_async(args=['makaimc'])
    return 'ok'
