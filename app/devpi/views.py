from flask import Blueprint, render_template

devpi = Blueprint('devpi', __name__,
                        template_folder='templates')
                        #static_folder='static')


@devpi.route('/')
def blueprint_subdomain():
    return render_template("devpi.html")

@devpi.route('/image')
def devpi_image():
    return render_template("devpi.html", show_image=True)