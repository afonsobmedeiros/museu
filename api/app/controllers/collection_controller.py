from app.services import collection_service as cs
from app.middleware.jwt_middleware import jwt_required
from bottle import Bottle, request, response

collection_controller = Bottle()


@collection_controller.post("/create/")
@jwt_required
def create():
    body: dict = request.json

    # validate data.
    if 'name' not in body or 'exhibition_id' not in body:
        response.status = 400
        return {"error": f"Missing 'name' or 'exhibition_id' in request body."}

    result = cs.create(**body)

    if not result:
        response.status = 401
        return {"error": "Invalid data."}

    return {
        "collection": {
            "id": result,
            "name": body["name"],
            "summary": body["summary"],
        }
    }


@collection_controller.put("/update/<collection_id:int>")
@jwt_required
def update(collection_id: int):
    body: dict = request.json

    # validate data.
    if 'name' not in body or 'summary' not in body:
        response.status = 400
        return {"error": f"Missing 'name' or 'summary' in request body."}

    result = cs.update(collection_id, **body)

    if not result:
        response.status = 401
        return {"error": "Invalid data."}
    response.status = 201
    return {
        "collection": {
            "id": result,
            "name": body["name"],
            "summary": body["summary"],
        }
    }
