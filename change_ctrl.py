import json
from flask import request
from flask_restful import Resource

# <<POST>>

class ChangeCtrl(Resource):
    def post(self):
        changectrl = request.json
        with open('changesctrl.json','r+') as ChangesCtrl:
            content = json.loads(ChangesCtrl.read())
            content.append(changectrl)
            ChangesCtrl.seek(0)
            ChangesCtrl.write(json.dumps(content, indent=4))
        return {'status': 'OK', 'message': 'Created'}, 201

# <<GET>>

    def get(self):
        with open('changesctrl.json','r') as ChangeCtrl:
            content = json.loads(ChangeCtrl.read())
            return content, 200