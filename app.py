from flask import Flask
import router


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.register_blueprint(router.bp)

    return app


if __name__ == "__main__":
    create_app().run()
