from django.http import HttpResponse
from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.event_handler.api_gateway import CORSConfig
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()
cors_config = CORSConfig(allow_origin="*")
app = APIGatewayRestResolver(cors=cors_config)

@app.get("/get")
def get_test():
    logger.info("Start API")
    return {"message": "API is working"}


@app.get("/hoge")
def get_todos():
    logger.info("Start API")
    event_dict = app.current_event.json_body
    return {"message": event_dict}

@logger.inject_lambda_context(
    log_event=True, correlation_id_path=correlation_paths.API_GATEWAY_REST
)

def lambda_handler(event: dict, context: LambdaContext) -> dict:
    logger.info(f"Received event: {event}")
    return app.resolve(event, context)