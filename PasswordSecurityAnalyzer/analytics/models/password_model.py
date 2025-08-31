class PasswordModel:
    def __init__(self, password):
        self.password = password
        self.analysis = {
            'length': len(password),
            'has_uppercase': any(c.isupper() for c in password),
            'has_lowercase': any(c.islower() for c in password),
            'has_numbers': any(c.isdigit() for c in password),
            'has_special': any(c in "!@#$%^&*()-_+=<>?{}[]|~`" for c in password),
            'is_strong': False
        }
        self.evaluate_strength()

    def evaluate_strength(self):
        criteria_met = sum([
            self.analysis['has_uppercase'],
            self.analysis['has_lowercase'],
            self.analysis['has_numbers'],
            self.analysis['has_special'],
            self.analysis['length'] >= 12
        ])
        self.analysis['is_strong'] = criteria_met >= 4

    def get_analysis(self):
        return self.analysis