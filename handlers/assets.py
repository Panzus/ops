# -*- coding: utf8 -*-


from handlers.base import BaseHandler


class AssetsGroupApi(BaseHandler):

    def get(self, name, *args, **kwargs):
        groups = {
            "networks": [],
            "projects": [
                {"id": 0, "pId": 0, "value": "ROOT", "assets_amount": 3, "tag": "projects"},
                {"id": 1, "pId": 0, "value": "上海", "assets_amount": 3, "tag": "projects"},
                {"id": 2, "pId": 0, "value": "深圳机房", "assets_amount": 4, "tag": "projects"},
                {"id": 3, "pId": 0, "value": "办公室", "assets_amount": 5, "tag": "projects"},
                {"id": 4, "pId": 1, "value": "产品线1", "assets_amount": 6, "tag": "projects"},
                {"id": 5, "pId": 2, "value": "产品线1", "assets_amount": 7, "tag": "projects"},
                {"id": 6, "pId": 3, "value": "产品线1", "assets_amount": 8, "tag": "projects"},
            ],
            "hosts": [],
            "domains": [],
        }
        self.finish({name: groups[name]})

    def post(self, asset, *args, **kwargs):
        pass


class Projects(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("projects.html")


class ProjectsApi(BaseHandler):
    def get(self, project, *args, **kwargs):
        pass

    def post(self, project, *args, **kwargs):
        pass


class Hosts(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("projects.html")


class HostsApi(BaseHandler):
    def get(self, host, *args, **kwargs):
        pass

    def post(self, host, *args, **kwargs):
        pass
