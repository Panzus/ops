# -*- coding: utf8 -*-


import configparser
import os
import logging

class ConfigParse(configparser.RawConfigParser):
    """
    配置对象
    """

    def __init__(self, file=None, logger=None):
        super(ConfigParse, self).__init__()
        self.logger = logger or logging.getLogger()
        config_file = self._config_file(file)
        self.read(config_file, encoding='utf8')

    def _config_file(self, file):
        """
        返回指定配置或者默认配置
        :param file: 配置文件
        :return: 配置文件或退出
        """
        cur_dir =  os.path.dirname(os.path.abspath('__file__'))
        default_config_dir = os.path.join(cur_dir, "conf")

        if file is None:
            file = os.path.join(default_config_dir, "server.ini")
            self.logger.debug("使用默认配置--{}".format(file))

        assert (os.path.exists(file) and os.path.isfile(file)), "配置文件不存在"
        return file

    def get_value(self, section, option):
        val = None
        try:
            val = self.get(section, option)
            #获取到的值为""
            if not val:
                val = None
        except Exception as e:
            self.logger.warning(e)
        return val

    def __getattr__(self, attr):
        if attr not in self.__dict__:
            return SectionAttr(attr, self)
        return self.__dict__[attr]


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
        return self.parent.get_value(self.section, option)







