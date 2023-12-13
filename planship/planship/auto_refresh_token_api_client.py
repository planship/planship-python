from planship_openapi_gen import ApiClient
from planship_openapi_gen.exceptions import UnauthorizedException

MAX_RETRIES = 3


class AutoRefreshTokenApiClient(ApiClient):
    def __init__(self, configuration, refresh_access_token) -> None:
        super().__init__(configuration)
        self.refresh_access_token = refresh_access_token

    def call_api(self, *args, **kwargs):
        retries = 0
        while retries < MAX_RETRIES:
            retries = +1
            try:
                return super().call_api(*args, **kwargs)
            except UnauthorizedException:
                print("401, refresh token and retry")
                self.configuration.access_token = self.refresh_access_token()
