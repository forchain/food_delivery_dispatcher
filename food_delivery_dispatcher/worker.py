from . import fleet 
from . import dbutil
from jsql import sql
from . import util

def dispatch():
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
        dispatch_result = dispatch_orders_to_delivery_drivers(delivery_drivers, orders)
        for id_food_order, id_delivery_driver in dispatch_result.items():
            sql(dbutil.engine, '''
            insert into delivery_task (
                id_food_order, id_delivery_driver
            ) values (
                :id_food_order, :id_delivery_driver
            )
            ''', id_food_order=id_food_order, id_delivery_driver=id_delivery_driver)

def dispatch_orders_to_delivery_drivers(delivery_drivers, orders):
    distance_matrix = []
    for delivery_driver in delivery_drivers:
        row = []
        for order in orders:
            row.append(util.geo_distance(delivery_driver['latitude'], delivery_driver['longitude'], order['restaurant_latitude'], order['restaurant_longitude']))
        distance_matrix.append(row)
    orders.sort(key=lambda x: x['placed_at'])
    result = dict()
    for i, order in enumerate(orders):
        min_distance = None
        min_driver = None
        for j, delivery_driver in enumerate(delivery_drivers):
            if min_distance is None or min_distance > distance_matrix[i][j]:
                min_distance = distance_matrix[i][j]
                min_driver = delivery_driver
                break
        if min_driver is not None:
            result[order['id_food_order']] = min_driver['id_delivery_driver']
    return result
