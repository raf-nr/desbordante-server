from internal.domain.user.token.access_token_manager import get_access_token_manager
from internal.domain.user.token.refresh_token_manager import get_refresh_token_manager

access_token_manager = get_access_token_manager()
refresh_token_manager = get_refresh_token_manager()
