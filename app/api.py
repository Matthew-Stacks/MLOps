# app/api.py
# FastAPI application endpoints.


from datetime import datetime
from functools import wraps
from http import HTTPStatus
from pathlib import Path
from typing import Dict, Optional

from fastapi import FastAPI, Request

from app import config
from app.config import logger
from app.schemas import PredictPayload
from tagifai import main, predict

# Define application
app = FastAPI(
    title="TagIfAI - Made With ML",
    description="Predict relevant tags given a text input.",
    version="0.1",
)


@app.on_event("startup")
def load_artifacts():
    global artifacts
    run_id = open(Path(config.MODEL_DIR, "run_id.txt")).read()
    artifacts = main.load_artifacts(run_id=run_id)
    logger.info("Ready for inference!")


def construct_response(f):
    """Construct a JSON response for an endpoint's results."""

    @wraps(f)
    def wrap(request: Request, *args, **kwargs):
        results = f(request, *args, **kwargs)

        # Construct response
        response = {
            "message": results["message"],
            "method": request.method,
            "status-code": results["status-code"],
            "timestamp": datetime.now().isoformat(),
            "url": request.url._url,
        }

        # Add data
        if "data" in results:
            response["data"] = results["data"]

        return response

    return wrap


@app.get("/", tags=["General"])
@construct_response
def _index(request: Request):
    """Health check."""
    return {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {},
    }


@app.post("/predict", tags=["Prediction"])
@construct_response
def _predict(request: Request, payload: PredictPayload) -> Dict:
    """Predict tags for a list of texts using the best run."""
    # Predict
    texts = [item.text for item in payload.texts]
    predictions = predict.predict(texts=texts, artifacts=artifacts)
    return {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {"predictions": predictions},
    }


@app.get("/params", tags=["Parameters"])
@construct_response
def _params(request: Request) -> Dict:
    """Get parameter values used for a run."""
    return {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {
            "params": vars(artifacts["params"]),
        },
    }


@app.get("/params/{param}", tags=["Parameters"])
@construct_response
def _param(request: Request, param: str) -> Dict:
    """Get a specific parameter's value used for a run."""
    return {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {
            "params": {
                param: vars(artifacts["params"]).get(param, ""),
            }
        },
    }


@app.get("/performance", tags=["Performance"])
@construct_response
def _performance(request: Request, filter: Optional[str] = None) -> Dict:
    """Get the performance metrics for a run."""
    performance = artifacts["performance"]
    if filter:
        for key in filter.split("."):
            performance = performance.get(key, {})
        data = {"performance": {filter: performance}}
    else:
        data = {"performance": performance}
    return {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": data,
    }
