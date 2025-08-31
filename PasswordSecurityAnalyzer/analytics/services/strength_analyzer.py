def analyze_password_strength(password):
    """
    Analyzes the strength of a given password and returns a score and feedback.

    Parameters:
    password (str): The password to analyze.

    Returns:
    dict: A dictionary containing the strength score and feedback.
    """
    score = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. Use at least 8 characters.")
    else:
        score += 1

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    # Check for lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    # Check for digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Include at least one digit.")

    # Check for special characters
    if any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    # Final feedback based on score
    if score < 3:
        feedback.append("Weak password.")
    elif score < 5:
        feedback.append("Moderate password.")
    else:
        feedback.append("Strong password.")

    return {
        "score": score,
        "feedback": feedback
    }