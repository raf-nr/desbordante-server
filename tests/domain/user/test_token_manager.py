import pytest
from datetime import timedelta, datetime, timezone
from uuid import uuid4

from internal.domain.user.token import access_token_manager, refresh_token_manager
from internal.domain.user.account_status_type import AccountStatusType
from internal.domain.user.permission import Permission
from internal.domain.user.token.access_token_manager import AccessTokenPayload
from internal.domain.user.token.general_token_manager import GeneralTokenManager
from internal.domain.user.token.refresh_token_manager import RefreshTokenPayload
from internal.domain.user.token.exception import (
    ExpiredTokenSignatureException,
    InvalidTokenSignatureException,
    DecodeTokenException,
)


@pytest.fixture
def access_token_payload() -> AccessTokenPayload:
    return AccessTokenPayload(
        user_id=uuid4(),
        session_id=uuid4(),
        device_id="device_123",
        exp=datetime.now(timezone.utc) + timedelta(minutes=30),
        email="test@example.com",
        account_status=AccountStatusType.EMAIL_VERIFICATION,
        permissions=[
            Permission.CAN_USE_OWN_DATASETS,
            Permission.CAN_MANAGE_USERS_SESSIONS,
        ],
    )


@pytest.fixture
def refresh_token_payload() -> RefreshTokenPayload:
    return RefreshTokenPayload(
        user_id=uuid4(),
        session_id=uuid4(),
        device_id="device_456",
        exp=datetime.now(timezone.utc) + timedelta(days=7),
    )


@pytest.mark.parametrize(
    "token_manager, token_payload_fixture",
    [
        (access_token_manager, "access_token_payload"),
        (refresh_token_manager, "refresh_token_payload"),
    ],
)
class TestTokenManager:
    def test_encode_token(
        self, token_manager: GeneralTokenManager, request, token_payload_fixture
    ):
        token_payload = request.getfixturevalue(token_payload_fixture)
        token = token_manager.encode(token_payload)
        assert isinstance(token, str)
        assert len(token) > 0

    def test_decode_token(self, token_manager, request, token_payload_fixture):
        token_payload = request.getfixturevalue(token_payload_fixture)
        token = token_manager.encode(token_payload)
        decoded_payload = token_manager.decode(token)

        assert decoded_payload.user_id == token_payload.user_id
        assert decoded_payload.session_id == token_payload.session_id
        assert decoded_payload.device_id == token_payload.device_id
        assert decoded_payload.exp != token_payload.exp

    def test_decode_expired_token(
        self, mocker, token_manager, request, token_payload_fixture
    ):
        token_payload = request.getfixturevalue(token_payload_fixture)

        # Mock the time for an expired token
        expired_time = datetime.now(timezone.utc) - timedelta(minutes=1)
        mocker.patch(
            "internal.domain.user.token.general_token_manager.datetime",
            mocker.Mock(now=lambda _: expired_time),
        )

        token = token_manager.encode(
            token_payload, time_expires_delta=timedelta(seconds=0)
        )

        with pytest.raises(ExpiredTokenSignatureException):
            token_manager.decode(token)

    def test_decode_invalid_signature(
        self, token_manager, request, token_payload_fixture
    ):
        token_payload = request.getfixturevalue(token_payload_fixture)

        token = token_manager.encode(token_payload)
        tampered_token = token[:-1] + "x"

        with pytest.raises(InvalidTokenSignatureException):
            token_manager.decode(tampered_token)

    def test_decode_invalid_payload(
        self, token_manager, request, token_payload_fixture
    ):
        token_payload = request.getfixturevalue(token_payload_fixture)

        token = token_manager.encode(token_payload)
        token_components = token.split(".")
        token_components[1] += "1"
        invalid_token = "".join(token_components)

        with pytest.raises(DecodeTokenException):
            token_manager.decode(invalid_token)
