import json

def borrar(posicion):
    with open('changesctrl.json',"r+") as ChangeCtrl:
        content = json.loads(ChangeCtrl.read())
        print(str(content))
        del content[posicion]
        ChangeCtrl.seek(0)
        ChangeCtrl.truncate()
        ChangeCtrl.write(json.dumps(content))
    return("Hola")
print(borrar(0))