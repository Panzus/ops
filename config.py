# -*- coding: utf8 -*-

import configparser
import os


class ConfigHandler(object):
    """
    配置解析
    """
    def __new__(cls, *args):
        if not hasattr(cls, '__instance'):
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance

    def __init__(self, path=None):
        config_path = self.config_file(path)
        self.c = configparser.RawConfigParser()
        self.c.read(config_path, encoding='utf8')

    def config_file(self, path):
        """
        返回指定配置或者默认配置
        :param path: 指定配置文件
        :return: 配置文件路径或退出
        """
        default_conf = os.path.join('conf', 'server.ini')
        default_conf_abs = os.path.join(
            os.path.dirname(os.path.abspath('__file__')),
            default_conf
        )
        if not path:
            path = default_conf_abs
            assert os.path.exists(path), '请确认配置文件'
        else:
            if not os.path.exists(path):
                path = default_conf_abs
                assert os.path.exists(path), '请确认配置文件'
        return path

    def get_value(self, section, option):
        """
        获取值
        :param section:
        :param option:
        :return:
        """
        try:
            val = self.c.get(section, option)
        except Exception as e:
            raise ValueError(e)
        return val

    def __getattr__(self, section):
        """
        动态创建方法 section
        :param section:
        :return:
        """
        return SectionAttr(section, self)


class SectionAttr(object):
    def __init__(self, section, parent):
        self.section = section
        self.parent = parent

    def __getattr__(self, option):
        """
        动态创建一个方法 option
        :param option:
        :return:
        """
        def run():
            return self.parent.get_value(self.section, option)
        return run


Config = ConfigHandler()
