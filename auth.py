def validate_user(username, password):
    if len(username.strip()) == 0 or len(password.strip()) == 0:
        return False
    if username == "admin" and password == "secret":
        return True
    return False
