# Generic example using Request lib to obtain OAuth2 Token

import requests
from requests_oauthlib import OAuth2Session


def main():
    client_id = "CLIENT_ID"
    # client_secret = "CLIENT_SECRET"
    redirect_url = "REDIRECT_URL"
    authorization_base_url = "URL_ENDPOINT_AUTH"
    token_url = "URL_DO_TOKEN"

    # OAuth session
    oauth2_session = OAuth2Session(client_id, redirect_url=redirect_url)
    auth_url, state = oauth2_session.authorization_url(authorization_base_url)

    # Users app Authorization and redirected
    authorization_response = input("Entre com a url de autorizacao: ")
    oauth_token = oauth2_session.fetch_token(
        token_url, authorization_response=authorization_response, state=state
    )
    assert oauth_token is not None


if __name__ == "__main__":
    main()
