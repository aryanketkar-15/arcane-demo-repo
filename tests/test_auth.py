from auth import validate_user

def test_validate_user_correct():
    assert validate_user("admin", "secret") is True

def test_validate_user_incorrect_password():
    assert validate_user("admin", "wrong") is False

def test_validate_user_incorrect_username():
    assert validate_user("wrong", "secret") is False

def test_validate_user_empty():
    assert validate_user("", "") is False

def test_validate_user_none():
    assert validate_user(None, None) is False
