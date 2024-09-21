from enum import StrEnum, auto


class Permission(StrEnum):
    CAN_USE_BUILTIN_DATASETS = auto()
    CAN_USE_OWN_DATASETS = auto()
    CAN_USE_USERS_DATASETS = auto()
    CAN_VIEW_ADMIN_INFO = auto()
    CAN_MANAGE_USERS_SESSIONS = auto()
    CAN_MANAGE_APP_CONFIG = auto()
