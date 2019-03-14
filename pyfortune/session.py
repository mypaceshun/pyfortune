import datetime
import requests
from bs4 import BeautifulSoup
from pyfortune.exception import (LoginFailureException,
                                 LoginRequireException)

LOGIN = 'login'
LOGOUT = 'logout'

class Session():
    """ログインセッションを張るためのクラス
    """
    def __init__(self):
        """初期化処理を行う
        """
        self.cookies = None
        self.BASE_URL = 'https://fortunemusic.jp/'
        self.LOGIN_URL = '{}default/login/'.format(self.BASE_URL)
        self.APPLY_LIST_URL = '{}mypage/apply_list/'.format(self.BASE_URL)

    def _pre_cookie(self):
        """事前にTOPページにアクセスし、Cookieを取得する
        """
        res = requests.get(self.BASE_URL)
        self.cookies = res.cookies

    def login(self, username, password):
        """ログイン処理を行う関数

        Args:
            username (str): ユーザー名
            password (str): パスワード

        Returns:
            str: ログインに成功したユーザー名

        Raises:
            pyfortune.exception.LoginfailureException

        Examples:
            >>> login('username', 'password')
            'username'
        """
        self._pre_cookie()
        data = {'login_id': username,
                'login_pw': password}
        res = requests.post(self.LOGIN_URL,
                            data=data,
                            cookies=self.cookies)
        self.cookies = res.cookies
        if self.status() is not LOGIN:
            res.text
            raise LoginFailureException('Login failure')
        return username

    def status(self):
        """ログインチェックを行う関数

        Returns:
            str: pyfortune.session.LOGINかpyfortune.session.LOGOUTが返される

        Examples:
            >>> status()
            'login'
        """
        res = requests.get(self.BASE_URL,
                    cookies=self.cookies)
        soup = BeautifulSoup(res.text, 'html.parser')
        logout_btn = soup.find('a', attrs={'class': 'btn01', 'href': '/default/logout/'})
        if logout_btn is None:
            return LOGOUT
        return LOGIN

    def fetch_apply_list(self, page=None):
        """抽選申し込み履歴の抽出

        Args:
            page (int): 申し込み履歴を抽出するpage番号、最初は0

        Returns:
            list: 申し込み情報の辞書のリスト

        Raises:
            pyfortune.session.LoginRequireException

        Examples:
            >>> fetch_apply_list()
            ['link': 'xxx', 'id': 'xxx', 'date': datetime.datetime(2018, 1, 1, 1, 1, 1), 'total_money': 1000, 'event': 'xxx', 'lottery_status': 'xxx', 'lottery_result': 'xxx', ...]
        """
        if self.status() is LOGOUT:
            raise LoginRequireException('Require Login')

        if page is None:
            page = 0
        res = requests.get('{}?page={}'.format(self.APPLY_LIST_URL, int(page)),
                           cookies=self.cookies)
        soup = BeautifulSoup(res.text, 'html.parser')
        tbody = soup.find('tbody')
        tr_list = tbody.findAll('tr')
        apply_list = []
        for tr in tr_list:
            td_list = tr.findAll('td')
            link = self.BASE_URL + td_list[0].find('a').get('href')
            id = td_list[0].find('a').text
            date = datetime.datetime.strptime(td_list[1].text[4:], '%Y-%m-%d %H:%M:%S')
            total_money = int(td_list[2].text[6:][:-1].replace(',', ''))
            event = td_list[3].text
            lottery_status = td_list[4].text[4:]
            lottery_result = td_list[5].text[4:]
            apply = {'link': link,
                     'id': id,
                     'date': date,
                     'total_money': total_money,
                     'event': event,
                     'lottery_status': lottery_status,
                     'lottery_result': lottery_result,}
            apply_list.append(apply)
        return apply_list
