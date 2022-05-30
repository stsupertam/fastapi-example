
import logging
from pathlib import Path

import uvicorn
from fastapi import FastAPI, Request

from src.custom_logging import CustomizeLogger

logger = logging.getLogger(__name__)

config_path=Path(__file__).with_name('logging_config.json')

def create_app() -> FastAPI:
    app = FastAPI(title='CustomLogger', debug=False)
    logger = CustomizeLogger.make_logger(config_path)
    app.logger = logger

    return app


app = create_app()

@app.get('/')
def logging_info(request: Request):
    return {'data': 'Hello World'}

@app.get('/log/info')
def logging_info(request: Request):
    request.app.logger.info('INFO LOGGING')
    return {'data': 'Successfully Implemented Info Log'}

@app.get('/log/warning')
def logging_warning(request: Request):
    request.app.logger.error('WARNING LOGGING')
    return {'data': 'Successfully Implemented Wanring Log'}

@app.get('/log/error')
def logging_error(request: Request):
    request.app.logger.info('ERROR LOGGING')
    return {'data': 'Successfully Implemented Error Log'}