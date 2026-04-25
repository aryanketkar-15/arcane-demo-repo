def validate_user(user, pwd):
    if not user or not pwd:
        return False
    if user == "admin" and pwd == "secret":
        return True
    return False
