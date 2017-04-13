# Import flask and template operators
from flask import Flask, render_template
from modules import helloworld

# Define the WSGI application object
app = Flask(__name__)

@app.route('/')
def page_root():
    return helloworld.hello_world()

# HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
