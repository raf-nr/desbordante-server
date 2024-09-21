from typing import Annotated

from passlib.context import CryptContext
from pydantic import StringConstraints


Password = Annotated[str, StringConstraints(min_length=8)]


class SecurityManager:

    def __init__(self):
        self.context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password: Password) -> Password:
        return self.context.hash(password)

    def verify_password(self, password: Password, hash_password: Password) -> bool:
        return self.context.verify(password, hash_password)


def get_security_manager() -> SecurityManager:
    return SecurityManager()
