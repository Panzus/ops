# -*- coding: utf-8 -*-


class BaseMethod:
    """ 通过Git 更新源码的job """

    slogin = None

    def __init__(self, name, user, passwd, url):
        self.name = name
        self.user = user
        self.passwd = passwd
        self.url = url


class Git(BaseMethod):
    slogin = "GIT"

class Svn(BaseMethod):
    slogin = "SVN"

