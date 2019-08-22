import json
from flask import request
from flask_restful import Resource

# <<POST>>

class Env(Resource):
    def post(self):
        environment = request.json
        with open('environments.json','r+') as environments:
            content = json.loads(environments.read())
            content.append(environment)
            environments.seek(0)
            environments.write(json.dumps(content, indent=4))
        return {'status': 'OK', 'message': 'Hecho'}, 201

# <<GET>>

    def get(self):
        with open('environments.json','r') as environments:
            content = json.loads(environments.read())
            return content, 200
