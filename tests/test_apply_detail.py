import os
import pytest
from tests.utils import (get_login_session,
                    get_session)
from pyfortune.exception import (LoginRequireException)


class TestFetchApplyDetail():
    def test_success_apply_detail(self):
        s = get_login_session()
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
        s = get_session()
        with pytest.raises(LoginRequireException):
            s.fetch_apply_detail(s.BASE_URL)

