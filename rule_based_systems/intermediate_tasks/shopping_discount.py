class ShoppingDiscountSystem:
    def __init__(self):
        self.rules = []
        self.orders = []

    def add_orders(self, item, price):
        self.orders.append({"item": item, "price": price})

    def add_rule(self,condition, discount):
        self.rules.append((condition, discount))

    @staticmethod
    def calculate_total(orders):
       return sum(order["price"] for order in orders)

    def apply_rule(self):
        total = self.calculate_total(self.orders)
        for condition, discount in self.rules:
            if condition(total):
                return discount
        return "No order found"


engine = ShoppingDiscountSystem()

engine.add_orders("clock", 12)
engine.add_orders("monitor", 45)
engine.add_orders("keyboard", 60)
engine.add_orders("lamp", 60)
engine.add_orders("mouse", 40)

engine.add_rule(lambda x: x < 100, "No discount")
engine.add_rule(lambda x: 100 <= x < 200, "10% discount")
engine.add_rule(lambda x: x > 200, "20% discount")

print(engine.apply_rule())