import time

from selenium.webdriver import Keys

from page.add_shopping_page import AddShoppingPage


class AddShoppingHandle(object):

    def __init__(self):
        self.asp = AddShoppingPage()

    # 商品数量加一
    def send_plus_one(self):
        return self.asp.get_plus()

    # 商品数量减一
    def send_minus_one(self):
        return self.asp.get_minus()

    # 加入购物车
    def click_cart(self):
        return self.asp.get_add_cart()

    # 清空数量
    def get_clear_quantity(self):
        self.asp.get_input('False')
        return self.asp.get_input().send_keys(Keys.DELETE)

    # 获取数量
    def get_quantity(self):
        time.sleep(1)
        return self.asp.get_input().get_attribute('value')

    # 购买商品数量等于库存数量
    def send_equal_stock(self):
        res = self.asp.get_stock()
        self.get_clear_quantity()
        return self.asp.get_input().send_keys(res)

    # 库存不足
    def send_stock_short(self):
        res = self.asp.get_stock()
        res = int(res) + 1
        self.get_clear_quantity()
        return self.asp.get_input().send_keys(res)

    # 切换框架
    def switch_frame(self, frame):
        if frame == 'next':
            return self.asp.switch_to()
        elif frame == 'up':
            return self.asp.switch_default_content()

    # 继续购物
    def continue_shopping(self):
        self.switch_frame('next')
        res = self.asp.go_on_shopping()
        self.switch_frame('up')
        return res

        # 去购物车结算
    def go_to_cart(self):
        self.switch_frame('next')
        return self.asp.go_to_cart_checkout()

    # 获取错误信息
    def get_info_error(self):
        return self.asp.get_shopping_error().get_attribute('textContent')

    # 获取商品名称
    def get_commodity_name(self, flag):
        if flag == '详情':
            return self.asp.get_details_commodity_name().get_attribute('textContent')
        elif flag == 'cart':
            return self.asp.get_cart_commodity_name().get_attribute('textContent')

    # 获取购物车商品数量
    def get_cart_quantity(self):
        return self.asp.get_cart_commodity_quantity().get_attribute('textContent')

if __name__ == '__main__':
    ash = AddShoppingHandle()
    ash.asp.bs.driver.get('http://tpshop.cn/Home/Goods/goodsInfo/id/237')
    res = ash.get_quantity()
    print('==============',res)
