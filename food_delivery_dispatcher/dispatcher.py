from . import util

def dispatch_orders_to_delivery_drivers(delivery_drivers, orders, distance_matrix):
    orders.sort(key=lambda x: x['placed_at'])
    result = dict()
    for i, order in enumerate(orders):
        min_distance = None
        min_driver = None
        for j, delivery_driver in enumerate(delivery_drivers):
            if min_distance is None or min_distance > distance_matrix[j][i]:
                min_distance = distance_matrix[j][i]
                min_driver = delivery_driver
        if min_driver is not None:
            result[order['id_food_order']] = min_driver['id_delivery_driver']
    return result

