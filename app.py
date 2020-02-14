from flask import Flask
from src.review_controller import reviews


def create_app():
    app = Flask(__name__)
    app.register_blueprint(reviews)

    @app.route('/')
    def start_here():
        return """Welcome to the index.<br>
        Search for reviews at '127.0.0.1:5000/review/${lending_tree_url}'<br>
        Ex: '127.0.0.1:5000/review/https://www.lendingtree.com/reviews/personal/cashnetusa/81638970'
        """

    return app


if __name__ == '__main__':
    create_app().run()