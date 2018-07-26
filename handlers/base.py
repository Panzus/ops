# -*- coding: utf-8 -*-


from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    def current_user(self):
        return "admin"

