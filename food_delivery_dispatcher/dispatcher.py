from . import util
import numpy as np
import concurrent.futures 
from concurrent.futures import ProcessPoolExecutor
from typing import Dict, List, Set, Tuple, Any
import os

def assign_drivers_to_orders(distance_table, batch_size):
    """
    Assign drivers to orders in batches
    
    Args:
        distance_table: List of (driver_id, order_id, distance) tuples
        batch_size: Maximum size of each batch
    
    Yields:
        List of (order_id, driver_id) assignments for each batch
    """
    assigned_drivers = set()
    assigned_orders = set()
    assignments = []
    current_size = 0

    for driver_id, order_id, distance in distance_table:
        if driver_id not in assigned_drivers and order_id not in assigned_orders:
            assignments.append((order_id, driver_id))
            assigned_drivers.add(driver_id)
            assigned_orders.add(order_id)
            current_size += 1
            
            # Yield assignments when batch size is reached
            if current_size >= batch_size:
                yield assignments
                assignments = []
                current_size = 0

    # Yield remaining assignments if any
    if assignments:
        yield assignments

def execute_delivery_task(order_id, driver_id):
    """
    Simulate the delivery action taken by the driver.
    """
    print(f"Driver {driver_id} starts delivering order {order_id}")

def process_batch(batch_assignments: List[Tuple[int, int]]) -> Dict[int, int]:
    """
    Process a single batch of order assignments
    Args:
        batch_assignments: List of (order_id, driver_id) pairs
    Returns:
        Dictionary mapping order IDs to driver IDs
    """
    worker_id = os.getpid()  # Get current process ID
    result = {}
    for order_id, driver_id in batch_assignments:
        print(f"Worker {worker_id} - Driver {driver_id} starts delivering order {order_id}")
        result[order_id] = driver_id
    return result

def dispatch_orders_to_delivery_drivers(
    delivery_drivers: List[Dict[str, Any]],
    orders: List[Dict[str, Any]],
    distance_matrix: List[List[float]],
    batch_size: int = 10,
    n_workers: int = os.cpu_count()
) -> Dict[int, int]:
    """
    Dispatch orders to delivery drivers in parallel
    
    Args:
        delivery_drivers: List of driver dictionaries containing driver info
        orders: List of order dictionaries containing order info
        distance_matrix: Distance matrix showing distances between drivers and restaurants
        batch_size: Maximum size of each batch for processing
        n_workers: Number of worker processes, defaults to system CPU count
    
    Returns:
        Dictionary mapping order IDs to driver IDs for the optimal assignment
    """
    if not orders or not delivery_drivers:
        return {}
    
    # Create distance table [(driver_id, order_id, distance), ...]
    distance_table = [
        (
            delivery_drivers[i]['id_delivery_driver'],
            orders[j]['id_food_order'],
            distance_matrix[i][j]
        )
        for i in range(len(delivery_drivers))
        for j in range(len(orders))
    ]
    distance_table.sort(key=lambda x: x[2])  # Sort by distance
    
    # Generate assignment plan using the algorithm
    all_assignments = list(assign_drivers_to_orders(distance_table, batch_size))
    
    # Get all order IDs from assignment plan
    all_orders = set(order_id for batch in all_assignments for order_id, _ in batch)
    result = {}

    # Use process pool to handle batches in parallel
    with ProcessPoolExecutor(max_workers=n_workers) as executor:
        # Submit batch tasks
        future_to_batch = {
            executor.submit(process_batch, batch): i 
            for i, batch in enumerate(all_assignments)
        }
        
        # Collect results
        for future in concurrent.futures.as_completed(future_to_batch):
            batch_index = future_to_batch[future]
            try:
                batch_result = future.result()
                result.update(batch_result)
            except Exception as e:
                print(f"Error processing batch {batch_index}: {e}")
    
    # Verify if all orders have been assigned
    assigned_orders = set(result.keys())
    unassigned_orders = all_orders - assigned_orders
    
    if unassigned_orders:
        print(f"Warning: {len(unassigned_orders)} orders were not assigned: {unassigned_orders}")
    
    return result
