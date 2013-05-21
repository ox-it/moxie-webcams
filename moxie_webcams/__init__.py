from flask import Blueprint

from .views import Webcams, StillImage


def create_blueprint(blueprint_name, conf):
    webcams_blueprint = Blueprint(blueprint_name, __name__, **conf)

    webcams_blueprint.add_url_rule('/', view_func=Webcams.as_view('webcams'))

    webcams_blueprint.add_url_rule('/<slug>', view_func=StillImage.as_view('webcam'))

    return webcams_blueprint