class AgeDeterminer:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, result):
        self.rules.append((condition, result))

    def apply_rule(self, age):
        for condition, result in self.rules:
            if condition(age):
                return  result
        return "Not Applicable"

engine = AgeDeterminer()

engine.add_rule(lambda x: 0 < x < 18, "Minor")
engine.add_rule(lambda x: x >= 18, "Adult")

print(engine.apply_rule(17))
print(engine.apply_rule(32))
print(engine.apply_rule(-1))