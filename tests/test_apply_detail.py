import os
import pytest
from pyfortune.session import Session
from pyfortune.exception import (LoginRequireException)

class TestFetchApplyDetail():
    def test_success_apply_detail(self):
        secrets_path = os.environ.get('SECRETS', 'secrets')
        with open(secrets_path, 'r') as f:
            lines = f.readlines()
            username = lines[0].strip()
            password = lines[1].strip()
        s = Session()
        s.login(username, password)
        a_list = s.fetch_apply_list()
        detail_list = s.fetch_apply_detail(a_list[0]['link'])
        assert isinstance(detail_list, list)
        assert len(detail_list) > 0
        detail = detail_list[0]
        must_keys = ['title', 'title_left',
                     'title_mid', 'title_right',
                     'one_money', 'subscription',
                     'winning', 'total_money']
        for k in must_keys:
            assert k in detail.keys()
    
    def test_untile_login(self):
        s = Session()
        with pytest.raises(LoginRequireException):
            s.fetch_apply_detail(s.BASE_URL)
