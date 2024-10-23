import pytest
import food_delivery_dispatcher.worker

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
    result = food_delivery_dispatcher.worker.dispatch_orders_to_delivery_drivers(delivery_drivers, food_orders)
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
    result = food_delivery_dispatcher.worker.dispatch_orders_to_delivery_drivers(delivery_drivers, food_orders)
    assert len(result) == 1
    assert result[1] == 2
