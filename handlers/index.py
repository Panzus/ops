# -*- coding: utf8 -*-


from handlers.base import BaseHandler


class Index(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")

    def post(self, *args, **kwargs):
        pass