import os
from pyfortune.session import Session


def get_login_session():
    secrets_path = os.environ.get('SECRETS', 'secrets')
    with open(secrets_path, 'r') as f:
        lines = f.readlines()
        username = lines[0].strip()
        password = lines[1].strip()
    s = Session()
    s.login(username, password)
    return s

def get_session():
    s = Session()
    return s
