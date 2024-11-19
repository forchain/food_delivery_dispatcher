# Food Delivery Dispatcher

## Introduction

We are providing an automatic dispatch system for a food delivery company.

The food delivery company has 2000 active delivery drivers, and handles 10000 orders per hour. During promotion, the number of orders may triple in a short period of time.

The dispatch system will assign food orders to delivery drivers every 15 seconds. Each food order can only be assigned to one driver and each driver can only deliver one order at a time.

The goal of the project is to minimize the distance between the drivers and the restaurants, while assigning as many orders as it can.

The input of driver and food order information are stored in the SQLite DB, and the result is saved in the delivery_task table in the same DB.

## Installation

### Prerequisites

1. Python 3.x
2. pip (Python package installer)

### Poetry Setup

1. Install Poetry:
```bash
pip install poetry==1.3.2
```

2. Install dependencies:
```bash
poetry update
```

Alternative installation without Poetry:
```bash
pip install -r requirements.txt
```

### Windows-specific Setup

1. Add Python Scripts folder to system PATH
   - Usually located at: `AppData\Roaming\Python\Scripts`
   - Or: `AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\Roaming\Python\Scripts`
   - Search for `poetry.exe` in AppData to find the correct folder

2. Enable long paths:
   - Open regedit
   - Navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem`
   - Change `longPathEnabled` value to 1

## Running the Application

Run the worker:
```bash
poetry run python3 -m food_delivery_dispatcher.main
```

Run the tests:
```bash
poetry run pytest
```

Without Poetry:
```bash
python -m pytest
```

## Data Model

The application uses SQLite database with the following tables:

### delivery_driver
Contains information about each delivery driver.

### fleet
Contains geographical groupings of drivers (e.g., Dubai fleet, Abu Dhabi fleet).

### user_state
Stores driver's current state:
- Current fleet
- Online status
- Current location (latitude and longitude)

### food_order
Contains customer order information:
- Restaurant location
- Customer location
- Order placement time
- Fleet mapping

### delivery_task
Contains current order-driver assignments (dispatcher output).

## Development

The project source code can be found in the following files:
- `dispatcher.py`: Main dispatch logic
- `tables.py`: Database table schemas
- `tests/`: Test cases

For more details about the implementation, please refer to the source code documentation.

