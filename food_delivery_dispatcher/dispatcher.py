from . import util

def dispatch_orders_to_delivery_drivers(delivery_drivers, orders, distance_matrix):
    '''
    assign drivers to orders in a FIFO manner. Will assign the closest driver to the earliest 
    created order and so on.
    '''
    orders.sort(key=lambda x: x['placed_at'])
    result = dict()
    used = set()
    for i, order in enumerate(orders):
        min_distance = None
        min_driver = None
        for j, delivery_driver in enumerate(delivery_drivers):
            if delivery_driver['id_delivery_driver'] not in used:
                if min_distance is None or min_distance > distance_matrix[j][i]:
                    min_distance = distance_matrix[j][i]
                    min_driver = delivery_driver
        if min_driver is not None:
            result[order['id_food_order']] = min_driver['id_delivery_driver']
            used.add(min_driver['id_delivery_driver'])
    return result

