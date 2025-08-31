import requests

def check_breach(password):
    # Mocked response for local testing
    # Always returns not breached
    return {"breached": False, "count": 0}

def is_password_breached(password):
    breached, count = check_breach(password)
    if breached:
        return f"Password has been breached {count} times."
    else:
        return "Password is safe."