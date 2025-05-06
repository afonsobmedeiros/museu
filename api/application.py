from config import DEBUG
from app import create_app


def main():
    application = create_app()
    try:
        application.run(reloader=DEBUG, debug=DEBUG)
    except SystemExit as e:
        if e == 3:
            application.run(reloader=DEBUG, debug=DEBUG)

if __name__ == '__main__':
    main()