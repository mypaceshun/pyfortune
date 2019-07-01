import os
import pytest
from tests.utils import (get_login_session,
                         get_session)
from pyfortune.exception import (LoginRequireException)

class TestFetchApplyList():
    def test_success_apply_list(self):
        s = get_login_session()
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
        s = get_session()
        with pytest.raises(LoginRequireException):
            s.fetch_apply_list()
