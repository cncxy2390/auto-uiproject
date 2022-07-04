import os
from datetime import datetime
import random


class FilePath(object):

    def __init__(self):
        self.file_path = os.path.dirname(os.path.abspath('__file__'))

    # 随机生成字符串
    def get_str(self):
        return ''.join(random.sample(['1','2','3','4','5','6','7','8','9','0'],6))

    # 获取当前时间
    def get_time(self):
        return datetime.now().strftime('%Y%m%d%H%M%S')

    # 测试数据
    def get_case(self):
        return self.file_path + '\datas\\'
        # print(path)

    # 测试数据
    def get_log(self):
        return self.file_path + '\logger\\'

    # 测试报告
    def get_report(self):
        return self.file_path + r'\test_result\report_html'

if __name__ == '__main__':
    print(FilePath().get_report())