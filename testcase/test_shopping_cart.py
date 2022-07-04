import time
import allure
import pytest

@allure.feature('购物车')
class TestShoppingCart(object):

    # 不选商品结算
    # @pytest.mark.skip
    @allure.story('不选商品结算')
    def test_not_choose(self, get_cart, get_logger, get_add_cart1):
        expected = '你的购物车没有选中商品'
        time.sleep(1)
        get_cart.sch.scp.bs.driver.get('http://tpshop.cn/Home/Cart/index')
        actual = get_cart.click_not_choose()
        get_logger.getLog(actual=actual, expected=expected)
        try:
            assert actual == expected
        except AssertionError as e:
            raise e


    # 商品数量必须大于0
    # @pytest.mark.skip
    @allure.story('商品数量必须大于0')
    def test_quantity_less_than(self, get_cart, get_logger, get_add_cart1):
        expected = '商品数量必须大于0'
        time.sleep(1)
        get_cart.sch.scp.bs.driver.get('http://tpshop.cn/Home/Cart/index')
        actual = get_cart.quantity_less_than()
        get_logger.getLog(actual=actual, expected=expected)
        try:
            assert actual == expected
        except AssertionError as e:
            raise e


    # 商品数量不能大于库存
    # @pytest.mark.skip
    @allure.story('商品数量不能大于库存')
    def test_greater_than_stock(self, get_cart, get_logger, get_add_cart1):
        expected = 'TPshop 努比亚 nubia X 双面屏 蓝金梵高 星空典藏版 8GB+512GB 全网通 移动联通电信4G手机 双卡双待商品数量不能大于86'
        time.sleep(1)
        get_cart.sch.scp.bs.driver.get('http://tpshop.cn/Home/Cart/index')
        actual = get_cart.greater_than_stock(86)
        get_logger.getLog(actual=actual, expected=expected)
        try:
            assert actual == expected
        except AssertionError as e:
            raise e


    # 购买商品数量不能大于200
    # @pytest.mark.skip
    @allure.story('购买商品数量不能大于200')
    def test_greater_than_two_hundred(self, get_cart, get_logger, get_add_cart2):
        expected = '购买商品数量不能大于200'
        time.sleep(1)
        get_cart.sch.scp.bs.driver.get('http://tpshop.cn/Home/Cart/index')
        actual = get_cart.greater_than_two_hundred(200)
        get_logger.getLog(actual=actual, expected=expected)
        try:
            assert actual == expected
        except AssertionError as e:
            raise e

    # 获取商品的小计
    # @pytest.mark.skip
    @allure.story('获取商品的小计')
    def test_subtotal(self, get_cart, get_logger, get_add_cart1):
        res = get_add_cart1.read_database(falg='one', sql="select goods_price from tp_cart where goods_name = 'TPshop 努比亚 nubia X 双面屏 蓝金梵高 星空典藏版 8GB+512GB 全网通 移动联通电信4G手机 双卡双待';")
        expected = int(res[0]['goods_price'])
        time.sleep(1)
        get_cart.sch.scp.bs.driver.get('http://tpshop.cn/Home/Cart/index')
        actual = get_cart.get_subtotal()
        actual = int(actual[:-20])
        get_logger.getLog(actual=actual, expected=expected)
        try:
            assert actual == expected
        except AssertionError as e:
            raise e

    # 获取商品的总价
    # @pytest.mark.skip
    @allure.story('获取商品的总价')
    def test_total(self, get_cart, get_logger, get_add_cart1):
        res = get_add_cart1.read_database(falg='one', sql="select sum(member_goods_price) price from tp_cart")
        expected = str(res[0]['price'])
        time.sleep(1)
        get_cart.sch.scp.bs.driver.get('http://tpshop.cn/Home/Cart/index')
        actual = get_cart.get_total()
        get_logger.getLog(actual=actual, expected=expected)
        try:
            assert actual == expected
        except AssertionError as e:
            raise e


    # 全部删除
    # @pytest.mark.skip
    @allure.story('全部删除')
    def test_delete_all(self, get_cart, get_logger, get_add_cart1):
        expected = '购物车空空的哦~，去看看心仪的商品吧~'
        time.sleep(1)
        get_cart.sch.scp.bs.driver.get('http://tpshop.cn/Home/Cart/index')
        actual = get_cart.delete_all()
        get_logger.getLog(actual=actual, expected=expected)
        try:
            assert actual == expected
        except AssertionError as e:
            raise e


    # 全部收藏
    # @pytest.mark.skip
    @allure.story('全部收藏')
    def test_collect_all(self, get_cart, get_logger, get_add_cart1):
        expected = '已添加至我的收藏'
        time.sleep(1)
        get_cart.sch.scp.bs.driver.get('http://tpshop.cn/Home/Cart/index')
        actual = get_cart.collect_all()
        get_logger.getLog(actual=actual, expected=expected)
        try:
            assert actual == expected
        except AssertionError as e:
            raise e

    # 删除单个
    # @pytest.mark.skip
    @allure.story('删除单个')
    def test_delete_one(self, get_cart, get_logger, get_add_cart1):
        expected = '购物车空空的哦~，去看看心仪的商品吧~'
        time.sleep(1)
        get_cart.sch.scp.bs.driver.get('http://tpshop.cn/Home/Cart/index')
        actual = get_cart.delete_one()
        get_logger.getLog(actual=actual, expected=expected)
        try:
            assert actual == expected
        except AssertionError as e:
            raise e

    # 收藏单个
    # @pytest.mark.skip
    @allure.story('收藏单个')
    def test_collect_one(self, get_cart, get_logger, get_add_cart1):
        expected = '已添加至我的收藏'
        time.sleep(1)
        get_cart.sch.scp.bs.driver.get('http://tpshop.cn/Home/Cart/index')
        actual = get_cart.collect_one()
        get_logger.getLog(actual=actual, expected=expected)
        try:
            assert actual == expected
        except AssertionError as e:
            raise e


    # 正常结算
    # @pytest.mark.skip
    @allure.story('正常结算')
    def test_success(self, get_cart, get_logger, get_add_cart1):
        expected = '订单信息'
        time.sleep(1)
        get_cart.sch.scp.bs.driver.get('http://tpshop.cn/Home/Cart/index')
        actual = get_cart.success_buy()
        get_logger.getLog(actual=actual, expected=expected)
        try:
            assert actual == expected
        except AssertionError as e:
            raise e

if __name__ == '__main__':
    pytest.main()