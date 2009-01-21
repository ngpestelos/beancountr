from couchdb import Server
from datetime import datetime
import re

db = Server()['beancountr']

pattern = re.compile(r'^(\d{4})(\d{2})(\d{2})$')

def process_date(d):
    coord = pattern.search(d).groups()
    dt = datetime(int(coord[0]), int(coord[1]), int(coord[2]))
    return dt.ctime()

def create(r):
    db.create({'type' : 'receipt', 'vendor' : r['vendor'], \
      'damage' : float(r['damage']), 'date' : process_date(r['date'])})
