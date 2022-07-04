import time
from common.bases import Bases
from common.logger import Logger


class AddShoppingPage(object):

    def __init__(self):
        self.bs = Bases()
        self.bs.login()
        self.bs.back_home()
        self.log = Logger()

    # 向下滑动
    def get_swipe_down(self):
        try:
            res = self.bs.driver.execute_script('window.scroll(0,500)')
        except Exception:
            self.log.getLog(element='"向下滑动"失败')
            raise
        return res

    # 选择商品
    def get_choose_commodity(self, commodity=7):
        try:
            self.bs.show_waiting(f'//div[contains(@class,"rmtj-list-main")]/div[{commodity}]', 'XPATH')
            res = self.bs.find_xpath(f'//div[contains(@class,"rmtj-list-main")]/div[{commodity}]').click()
            # res = self.bs.driver.find_element(by=By.XPATH, value=f'//div[contains(@class,"rmtj-list-main")]/div[{commodity}]').click()
        except Exception:
            self.log.getLog(element='查找"选择商品"失败')
            raise
        return res

    # 加入购物车
    def get_add_cart(self):
        try:
            self.bs.show_waiting('join_cart', 'ID')
            res = self.bs.find_id('join_cart').click()
            # res = self.bs.driver.find_element(by=By.ID, value='join_cart').click()
        except Exception:
            self.log.getLog(element='查找"加入购物车"失败')
            raise
        return res

    # 点击+号
    def get_plus(self):
        try:
            self.bs.show_waiting('//a[@class="add"]', 'XPATH')
            res = self.bs.find_xpath('//a[@class="add"]').click()
            # res = self.bs.driver.find_element(by=By.XPATH, value='//a[@class="add"]').click()
        except Exception:
            self.log.getLog(element='查找"+号"失败')
            raise
        return res

    # 点击-号
    def get_minus(self):
        try:
            self.bs.show_waiting('//a[@class="mins"]', 'XPATH')
            res = self.bs.find_xpath('//a[@class="mins"]').click()
            # res = self.bs.driver.find_element(by=By.XPATH, value='//a[@class="mins"]').click()
        except Exception:
            self.log.getLog(element='查找"-号"失败')
            raise
        return res

    # 获取库存
    def get_stock(self):
        try:
            self.bs.show_waiting('number', 'ID')
            res = self.bs.find_id('number').get_attribute('max')
            # res = self.bs.driver.find_element(by=By.ID, value='number').get_attribute('max')
        except Exception:
            self.log.getLog(element='查找"获取库存"失败')
            raise
        return res

    # 输入框
    def get_input(self, flag=True):
        if flag:
            try:
                self.bs.show_waiting('number', 'ID')
                res = self.bs.find_id('number')
                # res = self.bs.driver.find_element(by=By.ID, value='number')
                return res
            except Exception:
                self.log.getLog(element='查找元素失败')
                raise
        elif flag == False:
            try:
                self.bs.show_waiting('number', 'ID')
                res = self.bs.find_id('number').click()
                # res = self.bs.driver.find_element(by=By.ID, value='number').click()
            except Exception:
                self.log.getLog(element='查找"输入框"败')
                raise
            return res

    # 切换iframe
    def switch_to(self):
        try:
            self.bs.show_waiting('layui-layer-iframe1', 'ID')
            # res = self.bs.driver.switch_to.frame('layui-layer-iframe1')
            res = self.bs.switch_to_iframe('ayui-layer-iframe1')
        except Exception:
            self.log.getLog(element='"切换iframe"失败')
            raise
        return res

    # 返回第一层iframe
    def switch_default_content(self):
        try:
            # self.bs.driver.switch_to.default_content()
            self.bs.switch_default_content_iframe()
        except Exception:
            self.log.getLog(element='返回第一层iframe,查找元素失败')
            raise

    # 继续购物
    def go_on_shopping(self):
        try:
            self.bs.show_waiting('//a[contains(@class,"ui-button-f80")]', 'XPATH')
            res = self.bs.find_xpath('//a[contains(@class,"ui-button-f80")]').click()
            # res = self.bs.driver.find_element(by=By.XPATH, value='//a[contains(@class,"ui-button-f80")]').click()
        except Exception:
            self.log.getLog(element='查找"继续购物"失败')
            raise
        return res

    # 去购物车结算
    def go_to_cart_checkout(self):
        try:
            self.bs.show_waiting('//a[contains(@class,"ui-button-122")]', 'XPATH')
            res = self.bs.find_xpath('//a[contains(@class,"ui-button-122")]').click()
            # res = self.bs.driver.find_element(by=By.XPATH, value='//a[contains(@class,"ui-button-122")]').click()
        except Exception:
            self.log.getLog(element='查找"去购物车结算"失败')
            raise
        return res

    # 获取提示信息
    def get_shopping_error(self):
        try:
            self.bs.show_waiting('//div[@id="layui-layer2"]/div[2]', 'XPATH')
            res = self.bs.find_xpath('//div[@id="layui-layer2"]/div[2]')
            # res = self.bs.driver.find_element(by=By.XPATH, value='//div[@id="layui-layer2"]/div[2]')
        except Exception:
            self.log.getLog(element='查找"提示信息"失败')
            raise
        return res

    # 提示信息确认
    def get_info_confirm(self):
        try:
            self.bs.show_waiting('//div[@class="layui-layer-btn"]/a', 'XPATH')
            res = self.bs.find_xpath('//div[@class="layui-layer-btn"]/a').click()
            # res = self.bs.driver.find_element(by=By.XPATH, value='//div[@class="layui-layer-btn"]/a').click()
        except Exception:
            self.log.getLog(element='查找"提示信息确认"失败')
            raise
        return res

    # 立即购买
    def get_buy_now(self):
        try:
            self.bs.show_waiting('buy_now', 'ID')
            res = self.bs.find_id('//div[@class="layui-layer-btn"]/a').click()
            # res = self.bs.driver.find_element(by=By.ID, value='buy_now').click()
        except Exception:
            self.log.getLog(element='查找"立即购买"失败')
            raise
        return res

    # 获取购物车商品名称
    def get_cart_commodity_name(self):
        try:
            self.bs.show_waiting('//p[@class="msp_spname"]/a', 'XPATH')
            res = self.bs.find_xpath('//p[@class="msp_spname"]/a')
            # res = self.bs.driver.find_element(by=By.XPATH, value='//p[@class="msp_spname"]/a')
        except Exception:
            self.log.getLog(element='查找"获取购物车商品名称"失败')
            raise
        return res

    # 获取详情页商品名称
    def get_details_commodity_name(self):
        try:
            self.bs.show_waiting('//div[@class="detail-ggsl"]/h1', 'XPATH')
            res = self.bs.find_xpath('//div[@class="detail-ggsl"]/h1')
            # res = self.bs.driver.find_element(by=By.XPATH, value='//div[@class="detail-ggsl"]/h1')
        except Exception:
            self.log.getLog(element='查找"获取详情页商品名称"败')
            raise
        return res

    # 获取购物车商品数量
    def get_cart_commodity_quantity(self):
        try:
            time.sleep(2)
            res = self.bs.find_id('goods_num')
            # res = self.bs.driver.find_element(by=By.ID, value='goods_num')
        except Exception:
            self.log.getLog(element='查找"获取购物车商品数量"失败')
            raise
        return res