.. pyfortune documentation master file, created by
   sphinx-quickstart on Thu Mar 14 13:21:34 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyfortune's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   pyfortune

pyfortuneは某サイトへのスクレイピングを補助するツールです。

インストール
------------------------------------

::
   $ git clone https://github.com/mypaceshun/pyfortune
   $ cd pyfortune
   $ python setup.py install


クイックスタート
------------------------------------

ログイン処理のみを行う簡単なサンプルは以下の通りです ::
   >>> from pyfortune.session import Session
   >>> s = Session()
   >>> s.login('username', 'password')
   'username'

`status` 関数を利用することでログイン済みかどうかを確認出来ます。 ::
   >>> s.status()
   'login'


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
