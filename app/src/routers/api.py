from fastapi import APIRouter
from src.routers import log, sql, nosql

router = APIRouter()
router.include_router(log.router)
router.include_router(sql.router)
router.include_router(nosql.router)