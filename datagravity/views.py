from flask import request, render_template, jsonify

from . import app, db, redis_db, socketio
from .tasks import github_follower_count


@app.route('/', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')


@app.route('/refresh/github/', methods=['GET'])
def refresh_github():
    github_follower_count.apply_async(args=['makaimc'])
    return 'ok'
