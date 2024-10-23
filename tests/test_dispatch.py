import pytest
from food_delivery_dispatcher import util
import food_delivery_dispatcher.dispatcher

def test_dispatch_orders_to_delivery_drivers1():
    delivery_drivers = [{
        'id_delivery_driver': 1,
        'latitude': 2,
        'longitude': 2,
    }]
    food_orders = [{
        'id_food_order': 1,
        'order_nr': 'test1',
        'restaurant_latitude': 1,
        'restaurant_longitude': 1,
        'placed_at': '2024-01-01',
    }]
    distance_matrix = []
    for delivery_driver in delivery_drivers:
        row = []
        for order in food_orders:
            row.append(util.geo_distance(delivery_driver['latitude'], delivery_driver['longitude'], order['restaurant_latitude'], order['restaurant_longitude']))
        distance_matrix.append(row)
    result = food_delivery_dispatcher.dispatcher.dispatch_orders_to_delivery_drivers(delivery_drivers, food_orders, distance_matrix)
    assert len(result) == 1
    assert result[1] == 1

def test_dispatch_orders_to_delivery_drivers2():
    delivery_drivers = [{
        'id_delivery_driver': 1,
        'latitude': 2,
        'longitude': 2,
    }, {
        'id_delivery_driver': 2,
        'latitude': 1,
        'longitude': 1,
    }]
    food_orders = [{
        'id_food_order': 1,
        'order_nr': 'test1',
        'restaurant_latitude': 1,
        'restaurant_longitude': 1,
        'placed_at': '2024-01-01',
    }]
    distance_matrix = []
    for delivery_driver in delivery_drivers:
        row = []
        for order in food_orders:
            row.append(util.geo_distance(delivery_driver['latitude'], delivery_driver['longitude'], order['restaurant_latitude'], order['restaurant_longitude']))
        distance_matrix.append(row)
    result = food_delivery_dispatcher.dispatcher.dispatch_orders_to_delivery_drivers(delivery_drivers, food_orders, distance_matrix)
    assert len(result) == 1
    assert result[1] == 2

def get_distance_matrix(delivery_drivers, orders):
    return distance_matrix
