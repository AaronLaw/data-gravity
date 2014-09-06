import requests

from .models import Follower, Service
from datagravity import app, db, celery


@celery.task
def get_github_followers(username):
    """
        Returns the number of GitHub followers for a user name or
        False if there was an issue with the request.
    """
    service = Service.query.filter(Service.name=='GitHub')[0]
    resp = requests.get('https://api.github.com/users/%s' % username)
    if resp.status_code == requests.codes['OK']:
        f = Follower(service, resp.json()['followers'])
        db.session.add(f)
        db.session.commit()
    return resp.status_code

