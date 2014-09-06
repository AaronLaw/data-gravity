#!/usr/bin/env python
from gevent import monkey
monkey.patch_all()

import os

from datagravity import app, db, redis_db, celery, socketio
from datagravity.models import Service, Follower
from flask.ext.script import Manager, Shell
from loader import load

manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, redis_db=redis_db, celery=celery,
                Service=Service, Follower=Follower)

manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def syncdb():
    db.create_all()

@manager.command
def loaddb():
    load(db)

@manager.command
def runserver():
    socketio.run(app, "0.0.0.0", port=5001)


if __name__ == '__main__':
    manager.run()
