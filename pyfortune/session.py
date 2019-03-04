import requests
from bs4 import BeautifulSoup
from pyfortune.exception import LoginFailureException

LOGIN = 'login'
LOGOUT = 'logout'

class Session():
    def __init__(self):
        self.cookies = None
        self.BASE_URL = 'https://fortunemusic.jp/'
        self.LOGIN_URL = '{}default/login/'.format(self.BASE_URL)

    def _pre_cookie(self):
        res = requests.get(self.BASE_URL)
        self.cookies = res.cookies

    def login(self, username, password):
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
        res = requests.get(self.BASE_URL,
                    cookies=self.cookies)
        soup = BeautifulSoup(res.text, 'html.parser')
        logout_btn = soup.find('a', attrs={'class': 'btn01', 'href': '/default/logout/'})
        if logout_btn is None:
            return LOGOUT
        return LOGIN
