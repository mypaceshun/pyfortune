import requests
from bs4 import BeautifulSoup
from pyfortune.exception import LoginFailureException

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
            raise LoginFailureException()
        return username

    def status(self):
        """ログインチェックを行う関数

        Returns:
            str: `pyfortune.session.LOGIN`か`pyfortune.session.LOGOUT`が返される

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
