from bottle import Bottle
from .controllers.auth_controller import auth_controller
from .controllers.exhibition_controller import exhibition_controller
from .controllers.collection_controller import collection_controller
from .controllers.piece_controller import piece_controller



def create_app():
    app = Bottle()

    app.mount("/auth", auth_controller)
    app.mount("/exhibition", exhibition_controller)
    app.mount("/collection", collection_controller)
    app.mount("/piece", piece_controller)

    return app
