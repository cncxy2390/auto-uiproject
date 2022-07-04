import pytest
import allure

@allure.feature('商品详情')
class TestProductDetails(object):

    # 商品加一购买
    # @pytest.mark.skip
    @allure.story('商品加一购买')
    def test_add_one(self, get_pd, get_logger, get_clear_cart):
        expected = '2'
        get_pd.ash.asp.bs.driver.get('http://tpshop.cn/Home/Goods/goodsInfo/id/237')
        get_pd.add_one_commodity()
        actual = get_pd.get_commodity_quantity()
        get_logger.getLog(actual=actual, expected=expected)
        try:
            assert actual == expected
        except AssertionError as e:
            raise e

    # 商品减一购物
    # @pytest.mark.skip
    @allure.story('商品减一购物')
    def test_minus_one(self, get_pd, get_logger, get_clear_cart):
        expected = '1'
        get_pd.ash.asp.bs.driver.get('http://tpshop.cn/Home/Goods/goodsInfo/id/237')
        get_pd.add_one_commodity()
        get_pd.minus_one_commodity()
        actual = get_pd.get_commodity_quantity()
        get_logger.getLog(actual=actual, expected=expected)
        try:
            assert actual == expected
        except AssertionError as e:
            raise e


    # 商品数量等于库存数量购买
    # @pytest.mark.skip
    @allure.story('商品数量等于库存数量购买')
    def test_equal_stock(self, get_pd, get_logger, get_clear_cart):
        res = get_clear_cart.read_database(falg='one', sql="select store_count from tp_goods where goods_name = 'TPshop 努比亚 nubia X 双面屏 蓝金梵高 星空典藏版 8GB+512GB 全网通 移动联通电信4G手机 双卡双待'")
        expected = str(res[0]['store_count'])
        get_pd.ash.asp.bs.driver.get('http://tpshop.cn/Home/Goods/goodsInfo/id/237')
        actual = get_pd.equal_stock()
        get_logger.getLog(actual=actual, expected=expected)
        try:
            assert actual == expected
        except AssertionError as e:
            raise e

    # 购买商品库存不足
    # @pytest.mark.skip
    @allure.story('购买商品库存不足')
    def test_stock_short(self, get_pd, get_logger, get_clear_cart):
        res = get_clear_cart.read_database(falg='one', sql="select store_count from tp_goods where goods_name = 'TPshop 努比亚 nubia X 双面屏 蓝金梵高 星空典藏版 8GB+512GB 全网通 移动联通电信4G手机 双卡双待'")
        res = res[0]['store_count']
        expected = f'商品库存不足，剩余{res}'
        get_pd.ash.asp.bs.driver.get('http://tpshop.cn/Home/Goods/goodsInfo/id/237')
        actual = get_pd.stock_short()
        actual = actual.split(',')[0]
        get_logger.getLog(actual=actual, expected=expected)
        try:
            assert actual == expected
        except AssertionError as e:
            raise e

    # 正常加入购物车购买商品
    # @pytest.mark.skip
    @allure.story('正常加入购物车购买商品')
    def test_buy_commodity(self, get_pd, get_logger, get_clear_cart):
        expected = 'TPshop 努比亚 nubia X 双面屏 蓝金梵高 星空典藏版 8GB+512GB 全网通 移动联通电信4G手机 双卡双待'
        get_pd.ash.asp.bs.driver.get('http://tpshop.cn/Home/Goods/goodsInfo/id/237')
        actual = get_pd.buy_commodity()
        get_logger.getLog(actual=actual, expected=expected)
        try:
            assert actual == expected
        except AssertionError as e:
            raise e

if __name__ == '__main__':
    pytest.main()