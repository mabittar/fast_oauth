# OAuth Methods with Python

---

This repo track my studies about ways to implement oauth2 endpoints from third party sites


## GitHub

Following the documentation on GitHub it will be need a endpoint to user access and another one to callback response.
[GitHub Docs](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps#web-application-flow)


First create a **New OAuth App** at [Developer Settings > OAuth Apps](https://github.com/settings/developers)

Fill all information than copy the client Id and generate a new client secret.

This data will be used to fill env variables at `.env`


### Endpoints

the first one need to be a get, because when user access this endpoint will be automatic redirected to
`https://github.com/login/oauth/authorize`, I did that using RedirectResponse from starlette, to complete the request
you must inform the client_id as an params.

After the request is done, the callback will be pushed to the url + endpoint that you configured in your New OAuth App
on Github, or it could be configured as another param in the request. This callback will have code in the body.
After received the code in the body, create a new dict object to store the client_id, the client_secret and the code.
Create a new header dict obj with "Accept": "application/json" and make a new post request against
https://github.com/login/oauth/access_token` using your new params as request params and headers as headers of the request

Parse the json from the response and you will have the access_token to validate the Authorization Flow.
