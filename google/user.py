import logging
import pickle

from bot.services.database import add_user, update_user, delete_user, find_user
from google.default_methods import get_flow

logger = logging.getLogger(__name__)


def get_authorisation_url():

    flow = get_flow()
    auth_url, _ = flow.authorization_url(prompt='consent')
    return auth_url


def fetch_token(user_id, code):

    flow = get_flow()
    try:
        flow.fetch_token(code=code)
        credentials = flow.credentials
        save_user(user_id, credentials=pickle.dumps(credentials))
        return True
    except Exception as e:
        logger.exception(e, user_id=user_id, code=code)
        return False


def get_user_settings(user_id):
    return find_user(user_id)


def save_user(user_id, credentials):
    add_user(user_id, credentials)


def save_settings(user_id, credentials):
    update_user(user_id, credentials)


def del_user(user_id):
    delete_user(user_id)
