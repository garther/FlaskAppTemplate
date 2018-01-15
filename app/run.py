from flask import Flask

from index import views
from devpi import views
from tools import views

from index.views import index
from devpi.views import devpi
from tools.views import tools

from pprint import pprint

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(index)

# Subdomain blueprint
app.register_blueprint(devpi, subdomain='devpi')
app.add_url_rule('/static/<path:filename>', endpoint='static',
                subdomain='devpi', view_func=app.send_static_file)

# Route prefix blueprint
app.register_blueprint(tools, url_prefix='/tools')
app.add_url_rule('/static/<path:filename>', endpoint='static')#, 
                 #url_prefix='/tools', view_func=app.send_static_file)



from errors import *

if __name__ == '__main__':
    print(app.config['SERVER_NAME'])
    #app.run(host='0.0.0.0', port=5050)
    app.run()
