import math

class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(other):
        return math.sqrt(pow((self.x - other.x), 2) + pow((self.y - other.y), 2))

class Product(object):
    def __init__(self, product_type, weight):
        self.product_type = product_type
        self.weight = weight

class Order(object):
    def __init__(self, products, position):
        self.products = products
        self.position = position

class Warehouse(object):
    def __init__(self, products_quantities, position):
        self.products_quantities = products_quantities
        self.position = position

class Drone(object):
    def __init__(self, position, max_capacity):
        self.position = position
        self.max_capacity = max_capacity
        self.current_weight = 0
        self.current_products = {}

    def load(self, warehouse, product_type, quantity):
        pass

    def deliver(self, order):
        pass

    def unload(self, warehouse, product_type, quantity):
        pass

    def wait(self, turns):
        pass
