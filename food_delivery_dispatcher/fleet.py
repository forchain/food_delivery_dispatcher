from . import dbutil
from jsql import sql

def get_all_fleets():
    rows = sql(dbutil.engine, ''' select * from fleet ''').dicts()
    return list(map(lambda row: Fleet(row), rows))

class Fleet():
    def __init__(self, data):
        self.fleet_code = data['fleet_code']
        self.id_fleet = data['id_fleet']

