from pydantic import EmailStr

from internal.domain.user.account_status_type import AccountStatusType
from internal.domain.user.permission import Permission
from internal.domain.user.token.general_token_manager import (
    GeneralTokenPayload,
    GeneralTokenManager,
)


class AccessTokenPayload(GeneralTokenPayload):
    email: EmailStr
    account_status: AccountStatusType
    permissions: list[Permission]


class AccessTokenMager(GeneralTokenManager[AccessTokenPayload]):

    def __init__(self):
        super().__init__(token_payload_type=AccessTokenPayload)


def get_access_token_manager():
    return AccessTokenMager()
