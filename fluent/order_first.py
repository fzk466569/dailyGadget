#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: fzk
# @Time  18:39


from collections import namedtuple
from abc import ABCMeta, abstractmethod

Customer = namedtuple('Customer', 'name fidelity')


class LineItem(object):
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order(object):
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0.00
        else:
            discount = self.promotion.discount(self)

        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total:{total} due {due}>'
        return fmt.format(total=self.total(), due=self.due())


class Promotion(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def discount(self, order):
        # 返回折扣金额
        pass


class FidelityPromo(Promotion):
    # 为积分是1000以上用户提供5%折扣
    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    # 单个商品为20个或以上时提供10%折扣
    def discount(self, order):
        distinct = 0
        for item in order.cart:
            if item.quantity >= 20:
                distinct += 0.10 * item.total()
        return distinct


class LargeOrderPromo(Promotion):
    # 不同商品数量超过10个提供7%折扣
    def discount(self, order):
        items = {item.product for item in order.cart}
        return order.total() * 0.07 if len(items) >= 10 else 0


if __name__ == '__main__':
    fzk = Customer('fzk', 1000)
    wtt = Customer('wtt', 500)
    cart = [LineItem('apple', 5, 10), LineItem('pear', 10, 10), LineItem('banana', 50, 100)]
    o1 = Order(fzk, cart, FidelityPromo())
    o2 = Order(fzk, cart, BulkItemPromo())
    o3 = Order(fzk, cart, LargeOrderPromo())
    print(o1, o2, o3)
