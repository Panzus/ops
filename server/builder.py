# -*- coding: utf-8 -*-



class BaseBuilder:
    """ 构建工具"""

    def __init__(self, queues=None):

        self.queues = queues
        if self.queues is None:
            self.queues = []
            # 这个queues是否需要优化一下还要看后面的需求

    def isrunning(self):
        """ 检查当前编译器是否在运行
        """
        return False


