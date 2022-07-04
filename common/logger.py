import logging
from common.file_path import FilePath

class Logger(object):

    def __init__(self):
        path = FilePath()

        # 创建记录器
        self.logger = logging.getLogger()
        # 设置日志级别
        self.logger.setLevel(logging.DEBUG)

        # 控制台输出日志
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 日志写入位置
        self.fh = logging.FileHandler(path.get_log()+path.get_time()+path.get_str()+'.log', 'a', encoding='utf-8')
        # 设置日志级别
        self.fh.setLevel(logging.INFO)

        # 日志输入格式
        formatter = logging.Formatter('%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(self.fh)
        self.logger.addHandler(ch)

    def getLog(self, username=None, password=None, code=None, actual=None, expected=None, element=None):
        loggers = []
        loggers.append(self.logger.info('username:{username}'.format(username=username)))
        loggers.append(self.logger.info('password:{password}'.format(password=password)))
        loggers.append(self.logger.info('code:{code}'.format(code=code)))
        loggers.append(self.logger.info('Actual:{actual}'.format(actual=actual)))
        loggers.append(self.logger.info('Expected:{expected}'.format(expected=expected)))
        loggers.append(self.logger.info('Element:{element}'.format(element=element)))
        loggers.append(self.logger.error('Element:{element}'.format(element=element)))
        loggers.append(self.logger.info('-----------------------------------分割线-------------------------------------------'))
        return loggers

    def close_handler(self):
        self.logger.removeHandler(self.fh)
        self.fh.close()