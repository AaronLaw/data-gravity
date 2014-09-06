from datagravity.models import User, Follower, Service

def load(db):
    services = [Service("GitHub", "https://github.com/"),
                Service("Twitter", "https://twitter.com/"),]
    for s in services:
        db.session.add(s)
    db.session.commit()
