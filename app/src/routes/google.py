"""
Documentation
"""

from apiflask import APIBlueprint
from flask import render_template

google = APIBlueprint(
    "google",
    __name__,
    tag={
        "name": "Operations related to Google competitions.",
        "description": "",
    },
)


@google.route("/", methods=["GET"])
def api_get_google_competitions():
    """
    Renders /google
    """

    return render_template(
        "google.html",
        fullname="Andreas Stratakis",
        rank="unranked",
        nameholder="AS",
        active_page="google",
    )


@google.route("/codejam", methods=["GET"])
def api_get_google_codejam():

    return render_template(
        "google-codejam.html",
        fullname="Andreas Stratakis",
        rank="unranked",
        nameholder="AS",
        active_page="google",
    )


@google.route("/codejam/<year>", methods=["GET"])
def api_get_google_codejam_year(year: str):

    return render_template(
        "google-codejam-year.html",
        fullname="Andreas Stratakis",
        rank="unranked",
        nameholder="AS",
        active_page="google",
    )


@google.route("/kickstart", methods=["GET"])
def api_get_google_kickstart():

    return render_template(
        "google-kickstart.html",
        fullname="Andreas Stratakis",
        rank="unranked",
        nameholder="AS",
        active_page="google",
    )


@google.route("/hashcode", methods=["GET"])
def api_get_google_hashcode():

    return render_template(
        "google-hashcode.html",
        fullname="Andreas Stratakis",
        rank="unranked",
        nameholder="AS",
        active_page="google",
    )
