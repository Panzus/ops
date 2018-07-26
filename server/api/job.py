# -*- coding: utf-8 -*-


class JobMixin:
    """ 提供job的run方法， 这个系统最小的操作单元
    """

    def add_to_queues_by_hook(self, queues, job):
        """ 直接添加job到构建队列,提供一个触发的接口，还可以提供一个定时构建的功能 """
        pass

    def run(self, job):
        self.__update_source(job)

    def __update_source(self, job):
        """更新源码"""

        if job.slogin == "GIT":
            return self.__git(job)
        elif job.slogin == "SVN":
            return self.__svn(job)
        else:
            raise

    def __git(self, job):
        """ git 更新源码"""
        pass

    def __svn(self, job):
        """ svn 更新源码 """
        pass

    def build(self, base_path, JobName):
        """
        base_path: 源码保存目录
        JobName: job名称
        构建，怎么多语言构建，构建完成之后怎么自动下一步
        """
        job_abs_path = base_path + JobName

    @property
    def id(self):
        """ job ID """
        return

    @property
    def version(self):
        """ job 版本号 """
        return

