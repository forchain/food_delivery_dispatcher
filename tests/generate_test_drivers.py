import random
import json

def generate_test_drivers(count=100):
    drivers = []
    
    # Beijing latitude/longitude range
    lat_range = (33.3, 44.4)
    lng_range = (99.9, 111.1)
    
    for i in range(count):
        driver = {
            'id_delivery_driver': i + 1,
            'latitude': round(random.uniform(*lat_range), 6),
            'longitude': round(random.uniform(*lng_range), 6),
        }
        drivers.append(driver)
    
    return drivers

# Generate data
test_drivers = generate_test_drivers()

# Print first 5 and last 5 records as examples
print("First 5 records:")
print(json.dumps(test_drivers[:5], indent=2))
print("\nLast 5 records:")
print(json.dumps(test_drivers[-5:], indent=2))

# Output complete data
print("\nComplete data:")
print(json.dumps(test_drivers, indent=2))