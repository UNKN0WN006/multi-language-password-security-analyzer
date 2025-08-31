def calculate_password_strength(password):
    """Calculate the strength of a password based on length and character variety."""
    length_score = len(password) / 12  # Score based on length
    variety_score = (sum(1 for c in password if c.islower()) > 0) + \
                    (sum(1 for c in password if c.isupper()) > 0) + \
                    (sum(1 for c in password if c.isdigit()) > 0) + \
                    (sum(1 for c in password if c in "!@#$%^&*()_+") > 0)  # Special characters

    return min(length_score + variety_score, 1)  # Return a score between 0 and 1


def is_common_password(password):
    """Check if the password is in a predefined list of common passwords."""
    common_passwords = {"123456", "password", "123456789", "12345678", "12345", "1234567", "qwerty", "abc123"}
    return password in common_passwords


def format_suggestions(suggestions):
    """Format the suggestions for display."""
    return "\n".join(f"- {suggestion}" for suggestion in suggestions) if suggestions else "No suggestions available."