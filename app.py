from flask import Flask
import router
import error


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.register_blueprint(router.bp)
    error.error_handler(app)
    return app


if __name__ == "__main__":
    create_app().run()
