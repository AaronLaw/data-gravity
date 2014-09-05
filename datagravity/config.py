import os
from os import environ

basedir = os.path.abspath(os.path.dirname(__file__))

def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        var_set = environ[setting]
        if var_set == 'true' or var_set == 'True':
            return True
        elif var_set == 'false' or var_set == 'False':
            return False
        return var_set
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise Exception(error_msg)


DEBUG = get_env_setting('DEBUG')
SECRET_KEY = get_env_setting('SECRET_KEY')
REDIS_SERVER = get_env_setting('REDIS_SERVER')
REDIS_PORT = get_env_setting('REDIS_PORT')
REDIS_DB = get_env_setting('REDIS_DB')
TWILIO_ACCOUNT_SID = get_env_setting('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = get_env_setting('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = get_env_setting('TWILIO_NUMBER')
