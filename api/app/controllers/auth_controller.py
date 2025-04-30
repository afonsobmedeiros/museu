from bottle import Bottle, request, response

from app.services import authenticate_service

auth_controller = Bottle()


@auth_controller.post("/")
def authenticate():
    body: dict = request.json

    if "email" not in body or "password" not in body:
        response.status = 400
        return {"error": "Missing 'e-mail' and/or 'password' in request body."}

    result = authenticate_service.authenticate(body["email"], body["password"])

    if not result:
        response.status = 401
        return {"error": "Invalid credentials."}

    return result
