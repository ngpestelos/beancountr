from couchdb import Server
from datetime import datetime

db = Server()['beancountr']

def create(v):
    db.create({'type' : 'vendor', 'name' : v, \
      'posted' : datetime.today().ctime()})
