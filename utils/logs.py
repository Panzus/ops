import logging
import tornado.log
import os

from utils.config import ConfigParse


def create_default_logs():
    cur_path = os.path.dirname(os.path.abspath("__file__"))
    default_log_path = os.path.join(cur_path, "logs")
    if not os.path.exists(default_log_path):
        os.mkdir(default_log_path)

    _app_log_file = os.path.join(default_log_path, "app.log")
    if not os.path.exists(_app_log_file):
        os.mknod(_app_log_file)

    _access_log_file = os.path.join(default_log_path, "access.log")
    if not os.path.exists(_access_log_file):
        os.mknod(_access_log_file)


Config = ConfigParse()

log_levels = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warn": logging.WARN,
    "error": logging.ERROR
}

_log_level = Config.logs.level or 'debug'
log_level = log_levels.get(_log_level, logging.DEBUG)

# debug模式下所有日志都输出到stdout
log_to_stdout = Config.server.debug == 'True'

if log_to_stdout:
    app_handler = access_handler = logging.StreamHandler()
else:
    app_log_file = Config.logs.app_log
    access_log_file = Config.logs.access_log

    if (app_log_file is not None) and (access_log_file is not None):
        assert (os.path.exists(app_log_file)) and (os.path.exists(access_log_file))
    else:
        create_default_logs()
        app_log_file = os.path.join("logs", "app.log")
        access_log_file = os.path.join("logs", "access.log")

    app_handler = logging.FileHandler(app_log_file)
    access_handler = logging.FileHandler(access_log_file)

app_log = tornado.log.app_log
app_log.setLevel(log_level)
app_log_fmt = tornado.log.LogFormatter()
app_handler.setFormatter(app_log_fmt)
app_log.addHandler(app_handler)
# tornado.log.enable_pretty_logging(logger=app_log)

access_log = tornado.log.access_log
access_log.setLevel(log_level)
access_log.addHandler(access_handler)





