from flask import request, render_template, jsonify

from . import app, db, redis_db, socketio


@app.route('/', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

