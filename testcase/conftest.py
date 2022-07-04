import pytest
from business.admin.login_business import LoginBusiness
from business.login_reception_business import LoginReceptionBusiness
from business.shopping_business import ShoppingBusiness
from business.shopping_cart_business import ShoppingCartBusiness
from common.logger import Logger



# 后台登录
from common.read_datas import ReadDatas


@pytest.fixture(name='admin_login', scope='class')
def get_admin_login():
    lb = LoginBusiness()
    yield lb
    lb.lh.login.bs.driver.quit()

# 后台日志
@pytest.fixture(name='get_logger', scope='class')
def get_logger():
    # print("生成日志")
    log = Logger()
    yield log
    log.close_handler()

# 前台登录
@pytest.fixture(name='login', scope='class')
def get_login():
    lrb = LoginReceptionBusiness()
    yield lrb
    lrb.lh.lrp.bs.driver.quit()

# 商品详情
@pytest.fixture(name='get_pd', scope='class')
def get_product_details():
    sb = ShoppingBusiness()
    yield sb
    sb.ash.asp.bs.driver.quit()

# 购物车
@pytest.fixture(name='get_cart', scope='class')
def get_cart():
    scb = ShoppingCartBusiness()
    yield scb
    scb.sch.scp.bs.driver.quit()

# 数据库-清空购物车
@pytest.fixture(name='get_clear_cart')
def get_clear_cart():
    sb = ReadDatas()
    sb.read_database(falg='one', sql='DELETE FROM tp_cart')
    yield sb
    sb.read_database(falg='one', sql='DELETE FROM tp_cart')
    sb.close()

# 数据库-添加商品1到购物车
@pytest.fixture(name='get_add_cart1')
def get_add_cart1():
    sb = ReadDatas()
    sb.read_database(falg='one', sql='DELETE FROM tp_cart')
    sb.read_database(falg='one', sql="INSERT INTO tp_cart(id,user_id,goods_id,goods_sn,goods_name,market_price,goods_price,member_goods_price,goods_num,add_time) VALUES ('23','4725','237','24234234234','TPshop 努比亚 nubia X 双面屏 蓝金梵高 星空典藏版 8GB+512GB 全网通 移动联通电信4G手机 双卡双待','3988.00','2999.00','2789.07','1','1654163463');")
    yield sb
    sb.close()

# 数据库-添加商品2到购物车
@pytest.fixture(name='get_add_cart2')
def get_add_cart2():
    sb = ReadDatas()
    sb.read_database(falg='one', sql='DELETE FROM tp_cart')
    sb.read_database(falg='one', sql="INSERT INTO tp_cart(id,user_id,goods_id,goods_sn,goods_name,market_price,goods_price,member_goods_price,goods_num,add_time) VALUES ('24','4725','259','TP0000259','TPshop 分期免息 vivo U1全新vivou1限量版手机voviu1 y71vivo Y73步步高 ','1199.00','799.00','743.07','1','1654163937');")
    yield sb
    sb.close()