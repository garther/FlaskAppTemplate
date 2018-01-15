from flask import render_template, Blueprint, flash

tools = Blueprint('tools', __name__,
                        template_folder='templates')


@tools.route('/')
def tools_index():
    page = "index"
    return render_template("tools.html", tools=["asd", "bsd"])

@tools.route('/test', strict_slashes=False)
def tools_test():
    return render_template("tools.html", tools=["test", "test2"])