import pymysql

from common.read_configuration import ReadConfiguration


class ReadDatas(object):

    def __init__(self):
        get_mysql = ReadConfiguration()
        host = get_mysql.read_ini('mysql', 'host')
        user = get_mysql.read_ini('mysql', 'user')
        password = get_mysql.read_ini('mysql', 'password')
        database = get_mysql.read_ini('mysql', 'database')
        port = get_mysql.read_ini('mysql', 'port')
        charset = get_mysql.read_ini('mysql', 'charset')
        self.conn = pymysql.connect(host=host, user=user, password=password, database=database, port=int(port), charset=charset)
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    # 数据库
    def read_database(self, falg=None, sql=None):
        # 读取一行数据
        if falg == 'one':
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.conn.commit()
            return res

    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    rd = ReadDatas()
    res = rd.read_database(falg='one', sql="SELECT store_count from tp_goods where goods_name= 'TPshop 努比亚 nubia X 双面屏 蓝金梵高 星空典藏版 8GB+512GB 全网通 移动联通电信4G手机 双卡双待'")
    print(res[0]['store_count'])
    rd.close()