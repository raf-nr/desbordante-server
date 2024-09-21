from internal.domain.user.token.general_token_manager import (
    GeneralTokenPayload,
    GeneralTokenManager,
)


class RefreshTokenPayload(GeneralTokenPayload): ...


class RefreshTokenMager(GeneralTokenManager[RefreshTokenPayload]):

    def __init__(self):
        super().__init__(token_payload_type=RefreshTokenPayload)


def get_refresh_token_manager():
    return RefreshTokenMager()
