class NumberClassifier:
    def __init__(self):
        self.rules = []

    def add_rule(self, number, sign, type):
        self.rules.append((number, sign, type))

    def apply_rule(self, number_input):
        for number, sign, type in self.rules:
            if number(number_input):
                return f"{sign}, {'Even' if type(number_input) else 'Odd'}"
        return "Not applicable"


engine = NumberClassifier()

engine.add_rule(lambda x: x > 0, "Positive", lambda x: x % 2 == 0 )
engine.add_rule(lambda x: x < 0, "Negative", lambda x: x % 2 == 0 )
engine.add_rule(lambda x: x == 0, "Zero", lambda x: x % 2 == 0 )

print("Positive=>", engine.apply_rule(12))
print("Negative=> ", engine.apply_rule(-1223))
print("Zero=> ", engine.apply_rule(0))