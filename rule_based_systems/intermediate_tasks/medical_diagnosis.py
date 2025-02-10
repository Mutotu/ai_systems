class MedicalDiagnosisSystem:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, result):
        self.rules.append({"condition": condition, "result": result})

    def apply_rule(self, symptoms):
        symptom_set = set(symptoms.split(", "))  # Convert input to a set
        for rule in self.rules:
            rule_set = set(rule["condition"].split(", "))
            if symptom_set.issubset(rule_set) or rule_set.issubset(symptom_set):
                return rule["result"]
        return "Diagnosis Not Found"

# Initialize system
engine = MedicalDiagnosisSystem()

# Add medical rules
engine.add_rule("fever, cold", "Possible Flu")
engine.add_rule("fever", "Possible Heatstroke")
engine.add_rule("stomachache, vomit", "Possible Poisoning")

# Interactive user input
while True:
    symptoms = input("Enter symptoms (comma-separated), or 'x' to exit: ")
    if symptoms.lower() == "x":
        break
    formatted_symptoms = ", ".join(s.strip() for s in symptoms.split(","))
    print(engine.apply_rule(formatted_symptoms))
