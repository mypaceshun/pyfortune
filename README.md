# pyfortune

Fortune Musicをスクレイピングして情報を取得するためのライブラリ

# Install

## RequirePackage

* python3 (>=3.2)

## install command

```
$ python3 setup.py install
```

or

```
$ pip install .
```

PyPIには登録していないしする予定もない

# Usage

## クイックスタート

```
>>> from pyfortune.session import Session
>>> s = Session()
>>> s.status()
'logout'
>>> s.login('username', 'password')
'username'
>>> s.status()
'login'
```

## 詳細

### pyfortune.session.Session

ログイン等の処理を行うクラス

### pyfortune.session.Session.login(username, password)

ログイン処理を行う関数

ログインに成功した場合はユーザー名を返す。ログインに失敗した場合は`pyfortune.exception.LoginFailureException`を返す。

### pyfortune.session.Session.status()

ログイン状態を確認する関数

ログイン済みの場合は`'login'`を、未ログインの場合は`'logout'`を返す。
