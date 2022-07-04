import yaml
from configparser import ConfigParser

from common.file_path import FilePath


class ReadConfiguration(object):

    # 读取yaml文件
    def read_yaml(self,filename):
        path = FilePath()
        # print(path.get_case()+'login_data.yaml')
        with open(path.get_case()+filename, encoding='utf-8') as fp:
            get_yaml = yaml.load(fp, Loader=yaml.SafeLoader)
            return get_yaml

    # 读取ini文件
    def read_ini(self, section, option):
        path = FilePath()
        config = ConfigParser()
        config.read(path.get_case()+'database.ini')
        get_mysql = config[section][option]
        return get_mysql
