import time
from handle.shopping_cart_handle import ShoppingCartHandle


class ShoppingCartBusiness(object):

    def __init__(self):
        self.sch = ShoppingCartHandle()

    # 正常结算
    def success_buy(self):
        self.sch.click_paytotal('True')
        res = self.sch.get_hint('success')
        return res

    # 不选商品结算
    def click_not_choose(self):
        self.sch.click_opposite()
        time.sleep(1)
        self.sch.click_paytotal()
        res = self.sch.get_hint('notchoose')
        return res

    # 商品数量必须大于0
    def quantity_less_than(self):
        self.sch.send_quantity(0)
        self.sch.click_sum()
        res = self.sch.get_hint('collect')
        return res

    # 商品数量不能大于库存
    def greater_than_stock(self, stock):
        self.sch.send_quantity(stock)
        self.sch.click_sum()
        res = self.sch.get_hint('collect')
        return res

    # 购买商品数量不能大于200
    def greater_than_two_hundred(self, stock):
        self.sch.send_quantity(stock)
        self.sch.click_sum()
        time.sleep(1)
        res = self.sch.get_hint('collect')
        return res


    # 同一个商品，数量都多个
    # 多个商品，数量都是一个
    # 多个商品，数量都多个


    # 获取商品的小计
    def get_subtotal(self):
        res = self.sch.get_price('subtotal')
        return res



    # 获取商品的总价
    def get_total(self):
        res = self.sch.get_price('total')
        return res



    # 全部删除
    def delete_all(self):
        self.sch.click_all()
        self.sch.click_delete_all()
        res = self.sch.get_hint('null')
        res = res[6:-5]
        return res


    # 全部收藏
    def collect_all(self):
        self.sch.click_all()
        self.sch.click_collect_all()
        res = self.sch.get_hint('collect')
        return res

    # 删除单个
    def delete_one(self):
        self.sch.click_delete_one()
        res = self.sch.get_hint('null')
        res = res[6:-5]
        return res

    # 收藏单个
    def collect_one(self):
        self.sch.click_collect_one()
        res = self.sch.get_hint('collect')
        return res

if __name__ == '__main__':
    scb = ShoppingCartBusiness()
    time.sleep(1)
    scb.sch.scp.bs.driver.get('http://tpshop.cn/index.php/Home/Cart/index')
    scb.quantity_less_than()
