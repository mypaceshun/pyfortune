import os
import pytest
import pyfortune
from pyfortune.session import (Session,
                               LOGIN,
                               LOGOUT)
from pyfortune.exception import LoginFailureException


class TestLogin():
    def test_success_login(self):
        secrets_path = os.environ.get('SECRETS', 'secrets')
        with open(secrets_path, 'r') as f:
            lines = f.readlines()
            username = lines[0].strip()
            password = lines[1].strip()
        session = Session()
        res = session.login(username, password)
        assert res == username
        assert session.status() is LOGIN

    def test_bad_password(self):
        session = Session()
        with pytest.raises(LoginFailureException):
            res = session.login('bad_user_name', 'bad_user_password')
        assert session.status() is LOGOUT
