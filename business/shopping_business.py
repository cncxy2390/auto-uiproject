from handle.add_shopping_handle import AddShoppingHandle

class ShoppingBusiness(object):

    def __init__(self):
        self.ash = AddShoppingHandle()

    # 正常加入购物车购买商品
    def buy_commodity(self):
        self.ash.click_cart()
        self.ash.go_to_cart()
        res = self.ash.get_commodity_name('cart')
        return res


    # 商品加一购买
    def add_one_commodity(self):
        res = self.ash.send_plus_one()
        return res


    # 商品减一购物
    def minus_one_commodity(self):
        res = self.ash.send_minus_one()
        return res

    # 获取数量
    def get_commodity_quantity(self):
        return self.ash.get_quantity()

    # 商品数量等于库存数量购买
    def equal_stock(self):
        self.ash.get_clear_quantity()
        self.ash.send_equal_stock()
        self.ash.click_cart()
        self.ash.go_to_cart()
        res = self.ash.get_cart_quantity()
        return res

    # 购买商品库存不足
    def stock_short(self):
        self.ash.get_clear_quantity()
        self.ash.send_stock_short()
        self.ash.click_cart()
        self.ash.continue_shopping()
        self.ash.click_cart()
        res = self.ash.get_info_error()
        return res

if __name__ == '__main__':
    sb = ShoppingBusiness()
    sb.ash.asp.bs.driver.get('http://tpshop.cn/Home/Goods/goodsInfo/id/237')
    sb.stock_short()
