import os
import pytest
from tests.utils import get_login_session

class TestFetchApplyAllDetails():
    @pytest.mark.slow
    def test_fetch_some_apply_list(self):
        s = get_login_session()
        pagecount = 5
        all_apply_list = []
        for page in range(pagecount):
            apply_list = s.fetch_apply_list(page=page)
            all_apply_list = all_apply_list + apply_list
        assert len(all_apply_list) > 0

    @pytest.mark.slow
    @pytest.mark.parametrize(('page'), [p for p in range(5)])
    def test_fetch_some_detail_list(self, page):
        s = get_login_session()
        apply_list = s.fetch_apply_list(page=page)
        all_detail_list = []
        for apply in apply_list:
            detail_list = s.fetch_apply_detail(apply['link'])
            all_detail_list = all_detail_list + detail_list
        assert isinstance(all_detail_list, list)
