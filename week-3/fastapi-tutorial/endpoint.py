import json
from http import HTTPStatus

from pydantic import BaseModel
from starlette.responses import Response
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter()

class EventSchema(BaseModel):
    """Event Schema"""

    event_id: str
    event_type: str
    event_data: dict
    
# Create security scheme
security = HTTPBearer()

# In production, store this in environment variables
API_TOKEN = "this-is-a-test"

@router.post("/")
def handle_event(
    data: EventSchema,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    # Validate the token
    if credentials.credentials != API_TOKEN:
        raise HTTPException(
            status_code=401, 
            detail="Invalid authentication token"
        )
    
    # Process the valid request
    return {"message": "Data received!"}

"""
import json
from http import HTTPStatus

from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import Response


router = APIRouter()


class EventSchema(BaseModel):
    " ""Event Schema " ""

    event_id: str
    event_type: str
    event_data: dict


" ""
Becuase of the router, every endpoint in this file is prefixed with /events/
" ""


@router.post("/", dependencies=[])
def handle_event(
    data: EventSchema,
) -> Response:
    print(data)

    # Return acceptance response
    return Response(
        content=json.dumps({"message": "Data received!"}),
        status_code=HTTPStatus.ACCEPTED,
    )
"""
