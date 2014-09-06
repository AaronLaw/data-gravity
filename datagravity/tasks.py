import requests

from datagravity import app, db, celery

@celery.task
def get_github_followers(username):
    """
        Returns the number of GitHub followers for a user name or
        False if there was an issue with the request.
    """
    resp = requests.get('https://api.github.com/users/%s' % username)
    if resp.status_code == requests.codes['OK']:
        return resp.json()['followers']
    return False 
