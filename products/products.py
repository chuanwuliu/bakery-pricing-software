"""
This module defines the category of bakery products
"""


class Product(object):
    """
    Base Product class.
    """

    def __init__(self, name, code, units, price):
        self._name = name
        self._code = code
        self._units = units
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def code(self):
        return self._code

    @property
    def units(self):
        return self._units

    @property
    def price(self):
        return self._units

    def pack_info(self):
        return '{} $ {}'.format(self._units, self._price)


# class VegemiteScroll(Product):
#     """Concrete product: Vegemite scroll."""
#
#     def __init__(self, units, price):
#         self._name = 'Vegemite Scroll'
#         self._code = 'VS5'
#         super().__init__(units=units, price=price)
#
#
# class BlueberryMuffin(Product):
#     """Concrete product: Blueberry Muffin."""
#
#     def __init__(self, units, price):
#         self._name = 'Blueberry Muffin'
#         self._code = 'MB11'
#         super().__init__(units=units, price=price)
#
#
# class Croissant(Product):
#     """Concrete product: Croissant."""
#
#     def __init__(self, units, price):
#         self._name = 'Croissant'
#         self._code = 'CF',
#         super().__init__(units=units, price=price)
