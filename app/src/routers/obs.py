import io
import json
import os
import random
import uuid

from fastapi import APIRouter
from fastapi import Depends, HTTPException
from obs import ObsClient
from sqlalchemy.orm import Session

from src.common_libs.utils.logging import logger

OBS_ACCESS_KEY = os.getenv('OBS_ACCESS_KEY')
OBS_SECRET_KEY = os.getenv('OBS_SECRET_KEY')
OBS_END_POINT = os.getenv('OBS_END_POINT')
OBS_BUCKET_NAME = os.getenv('OBS_BUCKET_NAME')
OBS_TEST_FILE = os.getenv('OBS_TEST_FILE')

# Create an instance of ObsClient.
obsClient = ObsClient(
    access_key_id=OBS_ACCESS_KEY,    
    secret_access_key=OBS_SECRET_KEY,    
    server=OBS_END_POINT
)

def get_obs():
    try:
        yield obsClient
    finally:
        obsClient.close()


#APIRouter creates path operations for user module
router = APIRouter(
    prefix="/obs",
    responses={404: {"description": "Not found"}},
)

@router.get('/')
async def prediction(obs: ObsClient = Depends(get_obs)):
    json_result = None
    try:
        resp = obsClient.getObject(OBS_BUCKET_NAME, OBS_TEST_FILE, loadStreamInMemory=True) 
            
        if resp.status < 300: 
            buffer = resp.body.buffer
            json_result = json.load(io.BytesIO(buffer))  
    except:
        logger.error(traceback.format_exc())

    if json_result:
        return json_result
    else:
        raise HTTPException(status_code=404, detail="Cannot download file/ file not exist")