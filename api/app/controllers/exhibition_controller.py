from app.services import exhibition_service as es
from app.middleware.jwt_middleware import jwt_required
from bottle import Bottle, request, response

exhibition_controller = Bottle()


@exhibition_controller.post("/create/")
@jwt_required
def create():
    body: dict = request.json
    required_data = ["name", "start_at", "finish_at"]

    # validate data.
    for i in required_data:
        if i not in body:
            response.status = 400
            return {"error": f"Missing '{i}' in request body."}

    result = es.create(request.user_id, **body)

    if not result:
        response.status = 401
        return {"error": "Invalid data."}

    return {
        "exhibition": {
            "id": result,
            "name": body["name"],
            "summary": body["summary"],
            "start_at": body["start_at"],
            "finish_at": body["finish_at"],
        }
    }


@exhibition_controller.put("/update/<exhibition_id:int>")
@jwt_required
def update(exhibition_id: int):
    body: dict = request.json
    required_data = ["name", "start_at", "finish_at"]

    # validate data.
    for i in required_data:
        if i not in body:
            response.status = 400
            return {"error": f"Missing '{i}' in request body."}

    result = es.update(exhibition_id, **body)

    if not result:
        response.status = 401
        return {"error": "Invalid data."}

    return {
        "exhibition": {
            "id": result,
            "name": body["name"],
            "summary": body["summary"],
            "start_at": body["start_at"],
            "finish_at": body["finish_at"],
        }
    }
