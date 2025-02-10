class CustomerSupportSystem:
    def __init__(self):
        self.rules = []

    def add_rule(self, keywords, result):
        self.rules.append({"keywords": keywords, "result": result})

    def apply_rule(self, request):
        request_lower = request.lower()
        for rule in self.rules:
            if any(keyword in request_lower for keyword in rule["keywords"]):
                return rule["result"]
        return "Sorry, I didn't understand your request."

# Initialize system
engine = CustomerSupportSystem()

# Add support rules
engine.add_rule(["order", "status"], "Your order is being processed")
engine.add_rule(["refund", "policy"], "You can request a refund within 30 days")
engine.add_rule(["shipping", "delivery"], "Standard delivery takes 3-5 business days.")

# Interactive input loop
while True:
    user_request = input("Ask a question ('x' to exit): ")
    if user_request.lower() == "x":
        break
    print(engine.apply_rule(user_request))
