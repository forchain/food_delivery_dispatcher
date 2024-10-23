from . import fleet 
from . import util
import time
from . import dispatcher 
from . import dbutil
from jsql import sql
import logging

def dispatch():
    while True:
        print('dispatcher running...')
        for active_fleet in fleet.get_all_fleets():
            delivery_drivers = sql(dbutil.engine, '''
            select * from delivery_driver dd
            join user_state us using(id_delivery_driver)
            where us.id_fleet = :id_fleet
            ''', id_fleet=active_fleet.id_fleet).dicts()
            orders = sql(dbutil.engine, '''
            select * from food_order 
            where id_fleet = :id_fleet
            ''', id_fleet=active_fleet.id_fleet).dicts()
            print(f"assigning {len(orders)} orders to {len(delivery_drivers)} drivers for fleet {active_fleet.fleet_code}")
            distance_matrix = []
            for delivery_driver in delivery_drivers:
                row = []
                for order in orders:
                    row.append(util.geo_distance(delivery_driver['latitude'], delivery_driver['longitude'], order['restaurant_latitude'], order['restaurant_longitude']))
                distance_matrix.append(row)
            dispatch_result = dispatcher.dispatch_orders_to_delivery_drivers(delivery_drivers, orders, distance_matrix)
            for id_food_order, id_delivery_driver in dispatch_result.items():
                sql(dbutil.engine, '''
                insert into delivery_task (
                    id_food_order, id_delivery_driver
                ) values (
                    :id_food_order, :id_delivery_driver
                )
                ''', id_food_order=id_food_order, id_delivery_driver=id_delivery_driver)
        print('dispatcher sleeping...')
        time.sleep(15)

