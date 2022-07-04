import time
from selenium.webdriver.common.by import By
from common.bases import Bases
from common.logger import Logger


class ShoppingCartPage(object):

    def __init__(self):
        self.bs = Bases()
        self.bs.login()
        self.log = Logger()

    # 全选
    def get_all_choose(self, falg=False):
        if falg:
            try:
                self.bs.show_waiting('//div/i[contains(@class,"checkall")]', 'XPATH')
                res = self.bs.find_xpath('//div/i[contains(@class,"checkall")]')
                # res = self.bs.driver.find_elements(by=By.XPATH, value='//div/i[contains(@class,"checkall")]')
            except Exception:
                self.log.getLog(element='查找"全选"失败')
                raise
            return res
        else:
            try:
                self.bs.show_waiting('//div/i[contains(@class,"checkall")]', 'XPATH')
                res = self.bs.find_xpath('//div/i[contains(@class,"checkall")]').click()
                # res = self.bs.driver.find_element(by=By.XPATH, value='//div/i[contains(@class,"checkall")]').click()
            except Exception:
                self.log.getLog(element='查找"全选"失败')
                raise
            return res

    # 单选
    def get_only_choose(self):
        try:
            self.bs.show_waiting('//div[contains(@class,"meal-conts-name")]/div', 'XPATH')
            res = self.bs.find_xpath('//div[contains(@class,"meal-conts-name")]/div')
            # res = self.bs.driver.find_element(by=By.XPATH, value='//div[contains(@class,"meal-conts-name")]/div')
        except Exception:
            self.log.getLog(element='查找"单选"失败')
            raise
        return res

    # 删除选中商品
    def get_delete_all(self):
        try:
            self.bs.show_waiting('//div[@class="column"]/a[contains(@class,"deleteAll")]', 'XPATH')
            res = self.bs.find_xpath('//div[@class="column"]/a[contains(@class,"deleteAll")]')
            # res = self.bs.driver.find_element(by=By.XPATH, value='//div[@class="column"]/a[contains(@class,"deleteAll")]')
        except Exception:
            self.log.getLog(element='查找"删除选中商品"失败')
            raise
        return res

    # 删除
    def get_delete_one(self):
        try:
            self.bs.show_waiting('//div[contains(@class,"column")]/p/a[contains(@class,"deleteItem")]', 'XPATH')
            res = self.bs.find_xpath('//div[contains(@class,"column")]/p/a[contains(@class,"deleteItem")]')
            # res = self.bs.driver.find_element(by=By.XPATH, value='//div[contains(@class,"column")]/p/a[contains(@class,"deleteItem")]')
        except Exception:
            self.log.getLog(element='查找"删除"失败')
            raise
        return res

    # 确认删除
    def get_removeGoods(self):
        try:
            self.bs.show_waiting('removeGoods', 'ID')
            res = self.bs.find_id('removeGoods')
        except Exception:
            self.log.getLog(element='查找"确认删除"失败')
            raise
        return res

    # 移到我的收藏
    def get_collect_all(self):
        try:
            self.bs.show_waiting('//div[@class="column"]/a[contains(@class,"collectAll")]', 'XPATH')
            res = self.bs.find_xpath('//div[@class="column"]/a[contains(@class,"collectAll")]')
        except Exception:
            self.log.getLog(element='查找"移到我的收藏"失败')
            raise
        return res

    # 收藏单个商品
    def get_collect_one(self):
        try:
            self.bs.show_waiting('//div[contains(@class,"column")]/p/a[contains(@class,"collectItem")]', 'XPATH')
            res = self.bs.find_xpath(value='//div[contains(@class,"column")]/p/a[contains(@class,"collectItem")]')
        except Exception:
            self.log.getLog(element='查找"收藏单个商品"失败')
            raise
        return res

    # 商品名称
    def get_name(self):
        try:
            self.bs.show_waiting('//div[@class="breadth_phase"]/div/p[contains(@class,"msp_spname")]', 'XPATH')
            res = self.bs.find_xpath('//div[@class="breadth_phase"]/div/p[contains(@class,"msp_spname")]')
        except Exception:
            self.log.getLog(element='查找"商品名称"失败')
            raise
        return res

    # +号
    def get_sum(self):
        try:
            self.bs.show_waiting('//div[contains(@class,"quantity-form")]/a[@class="increment"]', 'XPATH')
            res = self.bs.find_xpath('//div[contains(@class,"quantity-form")]/a[@class="increment"]')
        except Exception:
            self.log.getLog(element='查找"+号"失败')
            raise
        return res

    # -号
    def get_minus(self):
        try:
            self.bs.show_waiting('//div[contains(@class,"quantity-form")]/a[@class="decrement"]', 'XPATH')
            res = self.bs.find_xpath('//div[contains(@class,"quantity-form")]/a[@class="decrement"]')
        except Exception:
            self.log.getLog(element='查找"-号"失败')
            raise
        return res

    # 数量
    def get_quantity(self):
        try:
            time.sleep(1)
            res = self.bs.find_xpath('//div[contains(@class,"quantity-form")]/input')
        except Exception:
            self.log.getLog(element='查找"数量"失败')
            raise
        return res

    # 单价
    def get_unit_price(self):
        try:
            self.bs.show_waiting('//div[@class="column t-price"]/span', 'XPATH')
            res = self.bs.find_xpath('//div[@class="column t-price"]/span')
        except Exception:
            self.log.getLog(element='查找"单价"失败')
            raise
        return res

    # 小计
    def get_subtotal(self):
        try:
            time.sleep(2)
            res =self.bs.find_xpath('//div[contains(@class,"item-single")]/div[contains(@class,"sumpri")]')
        except Exception:
            self.log.getLog(element='查找"小计"失败')
            raise
        return res


    # 总价
    def get_total_fee(self):
        try:
            time.sleep(1)
            res = self.bs.find_id('total_fee')
        except Exception:
            self.log.getLog(element='查找"总价"失败')
            raise
        return res

    # 去结算
    def get_paytotal(self):
        try:
            self.bs.show_waiting('//div[@class="butpayin"]/a', 'XPATH')
            res = self.bs.find_xpath('//div[@class="butpayin"]/a').click()
            # res = self.bs.driver.execute_script('document.getElementsByClassName("paytotal").click();')
        except Exception:
            self.log.getLog(element='查找"去结算"败')
            raise
        return res

    # 购物车为空
    # 为0获取大于库存提示
    def get_null_hint(self):
        try:
            self.bs.show_waiting('//div[@class="message"]/ul/li[contains(@class,"txt")]', 'XPATH')
            res = self.bs.find_xpath('//div[@class="message"]/ul/li[contains(@class,"txt")]')
        except Exception:
            self.log.getLog(element='查找"购物车为空"败')
            raise
        return res

    # 获取收藏提示、数量为0、数量为空
    def get_collect_hint(self):
        try:
            self.bs.show_waiting('//div[contains(@class,"layui-layer-padding")]', 'XPATH')
            res = self.bs.find_xpath('//div[contains(@class,"layui-layer-padding")]')
        except Exception:
            self.log.getLog(element='查找"获取收藏提示"失败')
            raise
        return res

    # 订单页面
    def get_order_page(self):
        try:
            res = self.bs.find_xpath('//div[@class="line-flowpath"]/span[contains(@class,"now")]')
        except Exception:
            self.log.getLog(element='查找"订单页面"失败')
            raise
        return res

    # 没有选择商品
    def get_not_commodity(self):
        try:
            res = self.bs.find_xpath('//div[@class="sd1"]/span')
        except Exception:
            self.log.getLog(element='查找"没有选择商品"失败')
            raise
        return res

if __name__ == '__main__':
    sch = ShoppingCartPage()
    time.sleep(5)
    sch.bs.driver.get('http://tpshop.cn/index.php/Home/Cart/index')
    # print(sch.get_subtotal())