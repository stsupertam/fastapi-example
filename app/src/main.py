import app_logger
from app_logger_formatter import CustomFormatter
from starlette.background import BackgroundTask

from fastapi import FastAPI, Request, Response
import uvicorn
from http import HTTPStatus

app = FastAPI()
formatter = CustomFormatter('%(asctime)s')
logger = app_logger.get_logger(__name__, formatter)
status_reasons = {x.value:x.name for x in list(HTTPStatus)}
    
def get_extra_info(request: Request, response: Response):
    return {'req': {
        'url': request.url.path,
        'headers': {'host': request.headers['host'],
                    'user-agent': request.headers['user-agent'],
                    'accept': request.headers['accept']},
        'method': request.method,
        'httpVersion': request.scope['http_version'],
        'originalUrl': request.url.path,
        'query': {}
        },
        'res': {'statusCode': response.status_code, 'body': {'statusCode': response.status_code,
                   'status': status_reasons.get(response.status_code)}}}

def write_log_data(request, response):
    logger.info(request.method + ' ' + request.url.path, extra={'extra_info': get_extra_info(request, response)})

@app.middleware("http")
async def log_request(request: Request, call_next):
    response = await call_next(request)
    response.background = BackgroundTask(write_log_data, request, response)
    return response


@app.get("/foo")
def foo(request: Request):
    return "success"