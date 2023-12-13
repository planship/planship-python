import planship_openapi_gen
from planship_openapi_gen.api.auth_api import AuthApi
from planship_openapi_gen.models import TokenResponse

from .auto_refresh_token_api_client import AutoRefreshTokenApiClient
from .http_basic_auth_configuration import HttpBasicAuthConfiguration


class Base:
    _url: str
    __client_id: str
    __client_secret: str
    __access_token: str = None

    def __init__(self, url: str, client_id: str, client_secret: str):
        self._url = url
        self.__client_id = client_id
        self.__client_secret = client_secret

    def __refresh_access_token(self) -> str:
        self.__access_token = self.get_access_token().access_token
        return self.__access_token

    def get_api_instance(self, api_class):
        if self.__access_token is None:
            self.__refresh_access_token()

        configuration = planship_openapi_gen.Configuration(
            host=self._url,
            access_token=self.__access_token,
        )

        with AutoRefreshTokenApiClient(
            configuration, self.__refresh_access_token
        ) as api_client:
            # Create an instance of the API class
            return api_class(api_client)

    def get_access_token(self) -> TokenResponse:
        configuration = HttpBasicAuthConfiguration(
            host=self._url,
            username=self.__client_id,
            password=self.__client_secret,
        )
        with planship_openapi_gen.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            auth_api = AuthApi(api_client)
            try:
                # Get Access Token
                api_response = auth_api.get_access_token()
                return api_response
            except Exception as e:
                print("Exception when calling AuthApi->get_access_token: %s\n" % e)
