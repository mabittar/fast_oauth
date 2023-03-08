from __future__ import annotations

from datetime import datetime, timedelta

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()
# this is an example only and must be change for others purposes
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="secret_token")


@app.get("/v1/users/{used_id}", tags=["users"])
async def get_user_data(used_id: int, authorization: str = Depends(oauth2_scheme)):
    return {"token": authorization}
