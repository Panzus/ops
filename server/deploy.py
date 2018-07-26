# -*- coding: utf-8 -*-


class Deploy:
    """
    发布job到环境，不管这个环境是测试还是开发都应该是一样的
    """

    def prepare(self):
        """ 准备运行job需要的环境，可以通过vcenter, openstack, K8s的接口创建
        """
        pass

    def check(self):
        """ 发布之后检查是否成功
        """
        return True

