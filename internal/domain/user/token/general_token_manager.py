from datetime import timedelta, datetime, timezone
from typing import Type, Self
from uuid import UUID

import jwt
from pydantic import BaseModel, ValidationError

from internal.domain.user import settings
from internal.domain.user.token.exception import (
    ExpiredTokenSignatureException,
    DecodeTokenException,
    InvalidTokenSignatureException,
    InvalidTokenException,
    InvalidTokenPayloadException,
)


class GeneralTokenPayload(BaseModel):
    user_id: UUID
    session_id: UUID
    device_id: str
    exp: datetime

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        return cls(**data)


class GeneralTokenManager[T: GeneralTokenPayload]:

    def __init__(self, token_payload_type: Type[T]):
        self._payloadType: Type[T] = token_payload_type

    def encode(self, payload: T, time_expires_delta: timedelta = timedelta(15)) -> str:
        payload_dict = payload.model_dump()
        expire = datetime.now(timezone.utc) + time_expires_delta
        payload_dict["exp"] = expire

        payload_dict = {
            k: (str(v) if isinstance(v, UUID) else v) for k, v in payload_dict.items()
        }

        token = jwt.encode(
            payload_dict,
            key=settings.token_secret_key,
            algorithm=settings.token_algorithm,
        )
        return token

    def decode(self, token: str) -> T:

        try:
            payload = jwt.decode(
                token,
                key=settings.token_secret_key,
                algorithms=[settings.token_algorithm],
            )
            return self._payloadType(**payload)
        except jwt.exceptions.ExpiredSignatureError:
            raise ExpiredTokenSignatureException()
        except jwt.exceptions.InvalidSignatureError:
            raise InvalidTokenSignatureException()
        except jwt.exceptions.DecodeError as e:
            raise DecodeTokenException(str(e))
        except jwt.exceptions.InvalidTokenError as e:
            raise InvalidTokenException(str(e))
        except ValidationError as e:
            raise InvalidTokenPayloadException(str(e))

    def get_token_expire(self, token: str) -> datetime:
        payload = self.decode(token)
        return payload.exp
