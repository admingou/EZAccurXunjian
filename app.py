from flask import Flask
from flask_cors import *
from EZAccur_xunjian_server.api.api_v1 import api


app = Flask(__name__)
CORS(app, supports_credentials=True)
app.register_blueprint(api)
# app.config.from_object(config)



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=7777,debug=False)