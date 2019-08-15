from environment import Env
from flask import Flask, jsonify
from change_ctrl import ChangeCtrl
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

api.add_resource(ChangeCtrl,'/changectrl')
api.add_resource(Env,'/environment')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")