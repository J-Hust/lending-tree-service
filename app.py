from flask import Flask
from src.review_controller import reviews


def create_app():
    app = Flask(__name__)
    app.register_blueprint(reviews)

    return app


if __name__ == '__main__':
    create_app().run()