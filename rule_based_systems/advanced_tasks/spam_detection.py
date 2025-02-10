class SpamDetectionSystem:
    def __init__(self):
        self.rules = []

    def add_rule(self, keywords, result, priority=1):
        self.rules.append({"keywords": keywords, "result": result, "priority": priority})
        self.rules.sort(key=lambda x: x["priority"], reverse=True)

    def apply_rule(self, spam):
        request_lower = spam.lower()
        for rule in self.rules:
            if any(keyword in request_lower for keyword in rule["keywords"]):
                return {"category": rule["result"], "confidence_score": 0.9}
        return {"category": "Not spam", "confidence_score": 1.0}

# Initialize system
engine = SpamDetectionSystem()

# Add rules with priorities
engine.add_rule(["win", "free", "click here"], "Mark as a spam", priority=3)
engine.add_rule(["discount", "sale"], "Mark as a promotion", priority=1)

# Test cases
print(engine.apply_rule("win a free trip"))   # {'category': 'Mark as a spam', 'confidence_score': 0.9}
print(engine.apply_rule("50% discount sale")) # {'category': 'Mark as a promotion', 'confidence_score': 0.9}
print(engine.apply_rule("Hello, how are you?")) # {'category': 'Not spam', 'confidence_score': 1.0}
