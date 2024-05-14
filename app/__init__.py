import os

from flask import Flask, jsonify, request
from models import load_models


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    # NOTE: models = load_models();
    load_models()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def success_response(data):
        return jsonify({"success": True, "data": data})

    def error_response(message, status_code=400):
        return jsonify({"success": False, "error": message}), status_code

    @app.route("/")
    def home():
        return jsonify({"message": "Welcome to the Flask RESTful API"})

    # a simple page that says hello

    @app.route("/hello/<name>")
    def hello(name):
        return jsonify({"message": f"Hello, {name}!"})

    @app.route("/api/training", methods=["GET"])
    def training():
        a = "true"
        try:
            if a == "atrue":
                raise ValueError("Result cannot be None")

            return success_response(["123", "21323", "fewfwe"])

        except:
            return error_response("error")

    @app.route("/api/predict", methods=["POST"])
    def predict_model():

        # NOTE:
        # model = models[model_name]
        try:
            data = request.json
            return success_response(["123", "21323", "fewfwe"])

        except:

            return error_response("error")

    return app
