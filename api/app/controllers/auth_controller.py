from bottle import Bottle, request, response

from app.services import authenticate_service
from app.middleware.cors_middleware import enable_cors

auth_controller = Bottle()


@auth_controller.route("/", method=['OPTIONS', 'POST'])
@enable_cors
def authenticate():
    body: dict = request.json
    print(body)
    if "email" not in body or "password" not in body:
        response.status = 400
        return {"error": "Missing 'e-mail' and/or 'password' in request body."}

    result = authenticate_service.authenticate(body["email"], body["password"])

    if not result:
        response.status = 401
        return {"error": "Invalid credentials."}

    return result
