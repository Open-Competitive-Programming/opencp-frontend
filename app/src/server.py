"""
Server
"""

import os

from apiflask import APIFlask, APIBlueprint
from flask import render_template

frontend = APIBlueprint(
    "frontend",
    __name__,
    tag={
        "name": "Frontend",
        "description": "Frontend Endpoints",
    },
)


@frontend.route("/", methods=["GET"])
def api_frontend_get_index():
    """
    Renders /
    """

    return render_template("index.html")


def create_app():
    """
    Creates the Flask application
    """

    app = APIFlask(__name__, spec_path="/specs", docs_path="/docs")
    app.secret_key = os.getenv("SECRET_KEY", "1234")
    app.config.from_prefixed_env()

    app.register_blueprint(frontend)

    app.config["settings"] = {
        "FLASK_RUN_HOST": os.getenv("FLASK_RUN_HOST", "0.0.0.0"),
        "FLASK_RUN_PORT": os.getenv("FLASK_RUN_PORT", "80"),
        "FLASK_DEBUG": os.getenv("FLASK_DEBUG", "True") == "True",
        "API_TITLE": os.getenv("API_TITLE", "Unknown"),
        "API_VERSION": os.getenv("API_VERSION", "0.0.0"),
        "SPEC_FORMAT": os.getenv("API_SPEC_FORMAT", "json"),
        "AUTO_SERVERS": os.getenv("API_AUTO_SERVERS", "True") == "True",
        "AUTO_TAGS": os.getenv("API_AUTO_TAGS", "False") == "True",
        "AUTO_OPERATION_SUMMARY": os.getenv("API_AUTO_OPERATION_SUMMARY", "True")
        == "True",
        "AUTO_OPERATION_DESCRIPTION": os.getenv(
            "API_AUTO_OPERATION_DESCRIPTION", "True"
        )
        == "True",
    }

    # Apply configuration settings for this API
    app.title = app.config["settings"]["API_TITLE"]
    app.version = app.config["settings"]["API_VERSION"]
    app.config["SECURITY_SCHEMES"] = {
        "BearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    }
    return app
