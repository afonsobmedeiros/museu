from config import DEBUG
from app import create_app


def main():
    application = create_app()
    
    application.run(reloader=DEBUG, debug=DEBUG)

if __name__ == '__main__':
    main()