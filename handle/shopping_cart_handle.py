import time
from selenium.webdriver import Keys
from page.shopping_cart_page import ShoppingCartPage

class ShoppingCartHandle(object):

    def __init__(self):
        self.scp = ShoppingCartPage()

    # 全选
    def click_all(self):
        self.scp.get_all_choose()
        # 获取按钮是否被选中 # True:获取多个元素  False:默认，获单个元素
        radios = self.scp.get_all_choose('True')
        for radio in radios:
            radio = radio.get_attribute('class')
            print(radio)
            radio = radio.split(' ')[-1]
            if radio != 'checkall-true':
                return self.scp.get_all_choose()
            else:
                break

    # 反选
    def click_opposite(self):
        time.sleep(0.5)
        self.scp.get_all_choose()
        # 获取按钮是否被选中 # True:获取多个元素  False:默认，获单个元素
        radios = self.scp.get_all_choose('True')
        for radio in radios:
            radio = radio.get_attribute('class')
            print(radio)
            radio = radio.split(' ')[-1]
            if radio != 'checkall-true':
                break
            else:
                return self.scp.get_all_choose()

    # 删除全部商品
    def click_delete_all(self):
        self.scp.get_delete_all().click()
        return self.scp.get_removeGoods().click()

    # 删除单个商品
    def click_delete_one(self):
        self.scp.get_delete_one().click()
        return self.scp.get_removeGoods().click()

    # 收藏全部商品
    def click_collect_all(self):
        return self.scp.get_collect_all().click()

    # 收藏单个商品
    def click_collect_one(self):
        return self.scp.get_collect_one().click()

    # 获取商品价格
    def get_price(self, flag):
        prices = 0
        # 单价
        if flag == 'unit':
            res = self.scp.get_unit_price().get_attribute('textContent')
            prices = res.split('￥')[-1]
        # 小计
        elif flag == 'subtotal':
            prices = self.scp.get_subtotal().get_attribute('textContent')
            prices = prices.split('￥')[-1]
        # 总价
        elif flag == 'total':
            res = self.scp.get_total_fee().get_attribute('textContent')
            prices = res.split('￥')[-1]
        return prices

    # 输入购买数量
    def send_quantity(self, number):
        self.scp.get_quantity().click()
        self.scp.get_quantity().send_keys(Keys.ARROW_LEFT)
        self.scp.get_quantity().send_keys(Keys.DELETE)
        self.scp.get_quantity().send_keys(Keys.DELETE)
        return self.scp.get_quantity().send_keys(number)

    # 点击加号
    def click_sum(self):
        return self.scp.get_sum().click()

    # 点击减号
    def click_minus(self):
        return self.scp.get_minus().click()

    # 获取提示信息
    def get_hint(self, flag):
        # 数量为空提示信息
        if flag == 'null':
            return self.scp.get_null_hint().get_attribute('textContent')
        # 收藏提示信息, 数量提示信息
        elif flag == 'collect':
            return self.scp.get_collect_hint().get_attribute('textContent')
        # 结算提示信息
        elif flag == 'success':
            res = self.scp.get_order_page().get_attribute('textContent')
            return res[-4:]
        # 没有选择商品
        elif flag == 'notchoose':
            return self.scp.get_not_commodity().get_attribute('textContent')


    # 点计去结算
    def click_paytotal(self, falg=False):
        if falg:
            self.click_all()
            res = self.scp.get_paytotal()
            self.scp.bs.get_alert()
            return res
        else:
            res = self.scp.get_paytotal()
            return res

if __name__ == '__main__':
    sch = ShoppingCartHandle()
    time.sleep(1)
    sch.scp.bs.driver.get('http://tpshop.cn/index.php/Home/Cart/index')
    # print(sch.send_quantity('201'))