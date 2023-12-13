from planship_openapi_gen import Configuration


class HttpBasicAuthConfiguration(Configuration):
    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        auth = {}
        if self.username is not None and self.password is not None:
            auth["HTTPBasicClientCredentials"] = {
                "type": "basic",
                "in": "header",
                "key": "Authorization",
                "value": self.get_basic_auth_token(),
            }
        return auth
