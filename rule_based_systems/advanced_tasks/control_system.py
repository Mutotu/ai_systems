class AccessControlSystem:
    def __init__(self):
        self.roles = {}

    def add_role(self, role, permissions):
        self.roles[role.lower()] = permissions

    def check_permission(self, role, action):
        role = role.lower()
        if role in self.roles and action in self.roles[role]:
            return f"Access granted: {role} can perform '{action}'"
        return f"Access denied: {role} cannot perform '{action}'"

access_system = AccessControlSystem()


access_system.add_role("Admin", {"read", "write", "delete"})
access_system.add_role("User", {"read"})
access_system.add_role("Guest", {"read limited"})

# Test cases
print(access_system.check_permission("Admin", "write"))
print(access_system.check_permission("User", "delete"))
print(access_system.check_permission("Guest", "read limited"))
print(access_system.check_permission("Guest", "write"))
