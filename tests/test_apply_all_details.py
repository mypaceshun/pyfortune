import os
import pytest
from pyfortune.session import Session
from pyfortune.exception import (LoginRequireException)

class TestFetchApplyAllDetails():
    @pytest.mark.slow
    def test_fetch_some_apply_list(self):
        secrets_path = os.environ.get('SECRETS', 'secrets')
        with open(secrets_path, 'r') as f:
            lines = f.readlines()
            username = lines[0].strip()
            password = lines[1].strip()
        s = Session()
        s.login(username, password)
        pagecount = 5
        all_apply_list = []
        for page in range(pagecount):
            apply_list = s.fetch_apply_list(page=page)
            all_apply_list = all_apply_list + apply_list
        assert len(all_apply_list) > 0

    @pytest.mark.slow
    @pytest.mark.parametrize(('page'), [p for p in range(5)])
    def test_fetch_some_detail_list(self, page):
        secrets_path = os.environ.get('SECRETS', 'secrets')
        with open(secrets_path, 'r') as f:
            lines = f.readlines()
            username = lines[0].strip()
            password = lines[1].strip()
        s = Session()
        s.login(username, password)
        apply_list = s.fetch_apply_list(page=page)
        all_detail_list = []
        for apply in apply_list:
            detail_list = s.fetch_apply_detail(apply['link'])
            all_detail_list = all_detail_list + detail_list
        assert isinstance(all_detail_list, list)
