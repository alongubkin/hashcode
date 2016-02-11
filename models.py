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

class Command(object):
    def __init__(self, drone):
        self.drone = drone

class LoadCommand(Command):
    def __init__(self, drone, warehouse, product_type, quantity):
        super(LoadCommand, self).__init__(self, drone, warehouse, product_type, quantity)
        self.warehouse = warehouse
        self.product_type = product_type
        self.quantity = quantity

class DeliverCommand(Command):
    def __init__(self, drone, order):
        super(DeliverCommand, self).__init__(self, drone, order)
        self.order = order

class UnloadCommand(Command):
    def __init__(self, drone, warehouse, product_type, quantity):
        super(UnloadCommand, self).__init__(self, drone, warehouse, product_type, quantity)
        self.warehouse = warehouse
        self.product_type = product_type
        self.quantity = quantity

class WaitCommand(Command):
    def __init__(self, drone, turns):
        super(WaitCommand, self).__init__(self, drone, turns)
        self.turns = turns

class Board(object):
    def __init__(self, width, height, drones, max_turns, products, warehouses,
                 orders):
        self.width = width
        self.height = height
        self.drones = drones
        self.max_turns = max_turns
        self.products = products
        self.warehouses = warehouses
        self.orders = orders


# parser.py
# input: txt file
# output: Board

# strategy.py
# input: Board
# output: Commands[]

# simulator.py
# input: Board, Commands[]
# output: Score
