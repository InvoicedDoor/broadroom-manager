from flask import Flask
from flask_cors import CORS

try:
    app = Flask(__name__)

    def init_app(config):
        try:
            app.config.from_object(config)
            app.register_blueprint()

            return app            
        except Exception as ex:
            print(ex)
            pass
except Exception as ex:
    print(ex)
    pass