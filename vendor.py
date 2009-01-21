from couchdb import Server
from datetime import datetime

db = Server()['beancountr']

def getAll():
    fun = '''
    function(doc) {
      if (doc.type == 'vendor')
        emit(doc.name, doc);
    }'''
    return [r.value for r in db.query(fun)]

def create(v):
    db.create({'type' : 'vendor', 'name' : v, \
      'posted' : datetime.today().ctime()})
