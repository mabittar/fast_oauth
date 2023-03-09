import httpx
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from fast_oauth.settings import EnvSettings

app = FastAPI()
settings = EnvSettings()
github_client_id = settings.github_client_id
github_client_secret = settings.github_client_secret


@app.get("/v1/github-login")
async def github_login():
    return RedirectResponse(
        f"https://github.com/login/oauth/authorize?client_id={github_client_id}",
        status_code=302,
    )


@app.get("/github-code")
async def github_code(code: str):
    req_params = {
        "client_id": github_client_id,
        "client_secret": github_client_secret,
        "code": code,
    }
    headers = {"Accept": "application/json"}
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url="https://github.com/login/oauth/access_token",
            params=req_params,
            headers=headers,
        )

    response_json = response.json()
    print(response_json)
    access_token = response_json["access_token"]
    async with httpx.AsyncClient() as client:
        headers.update({"Authorization": f"Bearer {access_token}"})
        response = await client.get(url="https://api.github.com/user", headers=headers)

    return response.json()
