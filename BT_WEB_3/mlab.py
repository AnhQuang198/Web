import mongoengine
# mongodb://<dbuser>:<dbpassword>@ds139470.mlab.com:39470/webc4e8
host = "ds139470.mlab.com"
port = 39470
db_name = "webc4e8"
username = "quanganh"
password = "quangquang"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=username, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())