from fastapi import FastAPI, Request
from app.routers import tasks
from prometheus_fastapi_instrumentator import Instrumentator
import logging
from loguru import logger
import json
import sys
import uuid
from dotenv import load_dotenv
from fastapi.responses import JSONResponse # To przyda się za chwilę

load_dotenv()
app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False}, root_path="/api")
Instrumentator().instrument(app).expose(app)

def format_log(record: dict) -> str:
    log_entry = {
        "@timestamp": record["time"].isoformat(),
        "log_level": record["level"].name,
        "message": record["message"]
    }

    if record["exception"]:
        log_entry["exception"] = str(record["exception"])
        
    log_entry.update(record["extra"])
    
    json_str = json.dumps(log_entry)
    return json_str.replace("{", "{{").replace("}", "}}") + "\n"


logger.remove() 
logger.add(sys.stdout, format=format_log)

class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1
        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(tasks.router)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = str(uuid.uuid4())

    with logger.contextualize(RequestId=request_id):
        logger.info(f"Received request: {request.method} {request.url.path}")
        response = await call_next(request)
        logger.info(f"Request return code: {response.status_code}")
        return response
    

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception(f"Uncaught exception: {request.url.path}")
    
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error."}
    )