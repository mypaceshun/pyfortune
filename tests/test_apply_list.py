import os
import pytest
from pyfortune.session import Session
from pyfortune.exception import (LoginRequireException)

class TestFetchApplyList():
    def test_success_apply_list(self):
        secrets_path = os.environ.get('SECRETS', 'secrets')
        with open(secrets_path, 'r') as f:
            lines = f.readlines()
            username = lines[0].strip()
            password = lines[1].strip()
        s = Session()
        s.login(username, password)
        result = s.fetch_apply_list()
        assert isinstance(result, list)
        assert len(result) > 0
        apply = result[0]
        must_keys = ['id', 'date', 'link',
                     'total_money', 'event',
                     'lottery_status', 'lottery_result']
        for k in must_keys:
            assert k in apply.keys()

    def test_untile_login(self):
        s = Session()
        with pytest.raises(LoginRequireException):
            s.fetch_apply_list()
