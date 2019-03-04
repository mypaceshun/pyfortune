
LOGIN = 'login'
LOGOUT = 'logout'

class Session():
    def __init__(self):
        pass

    def login(self, username, password):
        return username

    def status(self):
        return LOGIN
