from flask import Flask

from flaskr.controller import survey_controller

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("config.Config")

    app.register_blueprint(survey_controller.bp)

    return app