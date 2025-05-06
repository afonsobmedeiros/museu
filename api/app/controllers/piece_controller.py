from app.services import piece_service as ps
from app.middleware.jwt_middleware import jwt_required
from bottle import Bottle, request, response

piece_controller = Bottle()


@piece_controller.post("/create/")
@jwt_required
def create():
    body: dict = request.json

    # validate data.
    if 'subtitle' not in body or 'collection_id' not in body:
        response.status = 400
        return {"error": f"Missing 'subtitle' or 'collection_id' in request body."}

    result = ps.create(**body)

    if not result:
        response.status = 401
        return {"error": "Invalid data."}

    return {
        "piece": {
            "id": result,
            "summary": body["summary"],
            "subtitle": body["subtitle"],
            "summary": body["summary"],
            "part_date": body["part_date"],
            "photo": body["photo"],
            "photoPath": body["photoPath"]
        }
    }


@piece_controller.put("/update/<piece_id:int>")
@jwt_required
def update(piece_id: int):
    body: dict = request.json

    # validate data.
    if not body:
        response.status = 400
        return {"error": f"Missing data in request body."}

    result = ps.update(piece_id, **body)

    if not result:
        response.status = 401
        return {"error": "Invalid data."}

    response.status = 201
    return {
        "piece": {
            "id": result,
            "summary": body["summary"],
            "subtitle": body["subtitle"],
            "summary": body["summary"],
            "sartDate": body["partDate"],
            "photo": body["photo"],
            "photoPath": body["photoPath"]
        }
    }
