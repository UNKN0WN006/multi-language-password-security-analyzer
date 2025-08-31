import requests

def check_breach(password):
    url = f"https://api.pwnedpasswords.com/range/{password[:5]}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("Error fetching breach data")
    
    hashes = (line.split(':') for line in response.text.splitlines())
    for hash_suffix, count in hashes:
        if hash_suffix.lower() == password[5:].lower():
            return True, count
    
    return False, 0

def is_password_breached(password):
    breached, count = check_breach(password)
    if breached:
        return f"Password has been breached {count} times."
    else:
        return "Password is safe."