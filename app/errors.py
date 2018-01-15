from flask import render_template
from run import app


@app.errorhandler(404)
def page_not_found(e):
    return "Custom 404 baby!", 404