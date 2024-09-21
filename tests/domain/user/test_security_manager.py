from internal.domain.user.security import security_manager


def test_hash_password():
    password = "secure_password"
    hashed_password = security_manager.hash_password(password)

    assert isinstance(hashed_password, str)
    assert hashed_password != password


def test_hash_password_unique():
    password = "secure_password"
    hashed_password_1 = security_manager.hash_password(password)
    hashed_password_2 = security_manager.hash_password(password)

    assert hashed_password_1 != hashed_password_2


def test_verify_password_success():
    password = "secure_password"
    hashed_password = security_manager.hash_password(password)

    assert security_manager.verify_password(password, hashed_password)


def test_verify_password_failure():
    password = "secure_password"
    wrong_password = "wrong_password"
    hashed_password = security_manager.hash_password(password)

    assert not security_manager.verify_password(wrong_password, hashed_password)
