# pyfortune

Fortune Musicをスクレイピングして情報を取得するためのライブラリ

# Install

## RequirePackage

* python3 (>=3.2)

## install command

```
$ pip install py_fortune
```

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
