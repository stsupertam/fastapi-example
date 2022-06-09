from fastapi import APIRouter
from src.routers import log, sql, nosql, obs

router = APIRouter()
router.include_router(log.router)
router.include_router(sql.router)
router.include_router(nosql.router)
router.include_router(obs.router)