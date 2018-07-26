#!/usr/bin/python3
# -*- coding: utf8 -*-


import sqlite3

import tornado.httpserver
import tornado.ioloop
import tornado.web

from utils import Config, app_log
from urls import urls


settings = dict(
    cookie_secret=Config.server.cookie_secret,
    template_path=Config.server.template_path,
    static_path=Config.server.static_path,
    login_url=Config.server.login_url,
    xsrf_cookies='True' == Config.server.xsrf_cookies,
    debug='True' == Config.server.debug,
    )


class Application(tornado.web.Application):
    def __init__(self):
        super(Application, self).__init__(urls, **settings)

        self.sqlite = sqlite3.connect("fops.db")
        self.cursor = self.sqlite.cursor()

        self.maybe_create_tables()
        
    def maybe_create_tables(self):
        try:
            self.sqlite.cursor().execute("select * from nets")
        except sqlite3.OperationalError:
            self.cursor.execute("CREATE TABLE nets(id NOT NULL PRIMARY KEY, "
                                "name NOT NULL, net NOT NULL UNIQUE , region)")
            self.cursor.execute("CREATE TABLE ips(ip NOT NULL, host, in_use, net, PRIMARY KEY(ip, net))")

            self.sqlite.commit()


def main():
    app = Application()
    address = Config.server.address
    port = Config.server.port
    server = tornado.httpserver.HTTPServer(app)
    server.listen(port, address)
    app_log.info("server starting...")
    app_log.info("server listening on {}:{}".format(address, port))
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
