from fastapi import APIRouter
from src.routers import log, sql

router = APIRouter()
router.include_router(log.router)
router.include_router(sql.router)