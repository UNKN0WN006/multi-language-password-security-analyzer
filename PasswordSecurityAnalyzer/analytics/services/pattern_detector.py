def detect_patterns(password):
    patterns = {
        "sequential": False,
        "repeated": False,
        "common": False,
    }

    # Check for sequential characters
    if any(password[i] == password[i + 1] for i in range(len(password) - 1)):
        patterns["repeated"] = True

    # Check for common patterns (this can be expanded)
    common_patterns = ["123456", "password", "qwerty", "abc123"]
    if any(pattern in password for pattern in common_patterns):
        patterns["common"] = True

    # Check for sequential characters (e.g., abc, 123)
    for i in range(len(password) - 2):
        if (ord(password[i]) + 1 == ord(password[i + 1]) and
                ord(password[i + 1]) + 1 == ord(password[i + 2])):
            patterns["sequential"] = True
            break

    return patterns