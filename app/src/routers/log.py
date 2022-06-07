from fastapi import APIRouter

from src.common_libs.utils.logging import logger

#APIRouter creates path operations for user module
router = APIRouter(
    prefix="/log",
    responses={404: {"description": "Not found"}},
)

@router.get('/info')
async def info():
    logger.info("Info Route")
    return {"detail": "info"}

@router.get('/warning')
async def warning():
    logger.warning("Warning Route")
    return {"detail": "warning"}

@router.get('/error')
async def error():
    x = 1 / 0
    return {"detail": "error"}