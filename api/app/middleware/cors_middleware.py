from bottle import Bottle, request, response, HTTPResponse

def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # Set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, Authorization'
        response.headers['Access-Control-Allow-Credentials'] = 'true'

        # Respond to OPTIONS requests
        if request.method == 'OPTIONS':
            return {}

        return fn(*args, **kwargs)
    return _enable_cors
