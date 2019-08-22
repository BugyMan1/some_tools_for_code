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
            return content

# <<DELETE>>

    def delete(self, changectrl):
        with open('changesctrl.json',"r+") as ChangeCtrl:
            content = json.loads(ChangeCtrl.read())
            del content[int(changectrl)]
            ChangeCtrl.seek(0)
            ChangeCtrl.truncate()
            ChangeCtrl.write(json.dumps(content, indent=4))
        return {'status': 'OK', 'message': 'deleted'}, 200

# <<PUT>>

    def put(self, changectrl):
        changectrl_body = request.json
        with open('changesctrl.json',"r+") as ChangeCtrl:
            content = json.loads(ChangeCtrl.read())
            content[int(changectrl)] = changectrl_body
            ChangeCtrl.seek(0)
            ChangeCtrl.truncate()
            ChangeCtrl.write(json.dumps(content, indent=4))
        return {'status': 'OK', 'message': 'updated'}, 200



