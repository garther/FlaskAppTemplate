# Run a test server.
import config
from app import app
app.conf = config

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=config.DEBUG)
