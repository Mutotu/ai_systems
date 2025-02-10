class TrafficLightsDisplayer:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, result):
        self.rules.append({"condition": condition, "result": result})

    def apply_rule(self, text):
        for rule in self.rules:
            if rule["condition"] == text.lower():
                return rule["result"]
        return "No lights"

engine = TrafficLightsDisplayer()
engine.add_rule("red", "Stop")
engine.add_rule("yellow", "Get Ready")
engine.add_rule("green", "Go")


while True:
    color = input("Add color 'x' to exit : ")
    if color.lower() == 'x':
        break
    result = engine.apply_rule(color)
    print(result)