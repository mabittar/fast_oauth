import unittest

import requests_mock
from requests_oauthlib import OAuth2Session


class TestOauth2(unittest.TestCase):
    def setUp(self) -> None:
        self.client_id = "SEU_CLIENT_ID"
        self.client_secret = "SEU_CLIENT_SECRET"
        self.redirect_uri = "https://url_de_testes_redirect"
        self.authorization_base_url = "https://url_de_teste_auth"
        self.token_url = "https://url_de_teste_toekn"

        self.mock_response = {
            "access_token": "ACCESS_TOKEN",
            "token_type": "bearer",
            "expires_in": 360,
            "refresh_token": "REFRESH_TOKEN",
            "scope": "SCOPE",
        }

    def test_oauth2(self):
        with requests_mock.Mocker() as m:
            # Mock da autrizaćão
            m.get(self.authorization_base_url, text="")

            # Mock da resposta de token
            m.post(self.token_url, json=self.mock_response)

            # Criar sessão OAuth2
            oauth2_session = OAuth2Session(
                self.client_id, redirect_uri=self.redirect_uri
            )
            authorization_url, state = oauth2_session.authorization_url(
                self.authorization_base_url
            )

            # Simular redirecionamento do usuário para a URL de autorização
            authorization_response = "https://localhost:8000/?code=1234"
            oauth2_token = oauth2_session.fetch_token(
                self.token_url,
                authorization_response=authorization_response,
                client_secret=self.client_secret,
                state=state,
            )

            self.assertEqual(oauth2_token["access_token"], "ACCESS_TOKEN")
            self.assertEqual(oauth2_token["refresh_token"], "REFRESH_TOKEN")
            self.assertEqual(oauth2_token["expires_in"], 3600)
            self.assertEqual(oauth2_token["token_type"], "bearer")
            self.assertEqual(oauth2_token["scope"], "SCOPE")


if __name__ == "__main__":
    unittest.main()
