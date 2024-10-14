import hashlib
import hmac
import re
import time

from fastapi import Depends, FastAPI, Request
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from .models import OutlineSignInEvent
from .utils import SettingsDepend

app = FastAPI()


async def check_webhook_signature(request: Request, settings: SettingsDepend):
    signature = request.headers.get("outline-signature")
    if not signature:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="Missing signature"
        )
    matched = re.match(r"^t=([0-9]+),s=([0-9a-f]+)$", signature)
    if not matched:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="Invalid signature format"
        )
    timestamp, signature = matched.groups()
    if abs(time.time() * 1000 - int(timestamp)) > settings.timedelta_seconds:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="Expired signature"
        )
    request_body_digest = hmac.new(
        settings.outline_webhook_secret,
        f"{timestamp}.".encode() + await request.body(),
        hashlib.sha256,
    ).hexdigest()
    if not hmac.compare_digest(
        request_body_digest.casefold(),
        signature.casefold(),
    ):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="Invalid signature digest"
        )
    return


@app.post("/webhook", dependencies=[Depends(check_webhook_signature)])
async def webhook(event: OutlineSignInEvent):
    pass
