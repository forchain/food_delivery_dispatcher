import random
from datetime import datetime, timedelta
import json

def generate_test_orders(count=99):
    orders = []
    start_date = datetime(2024, 1, 1)
    
    # 北京市的大致经纬度范围
    lat_range = (39.8, 40.2)  # 纬度范围
    lng_range = (116.2, 116.6)  # 经度范围
    
    for i in range(count):
        # 生成随机日期(1-90天内)
        random_days = random.randint(0, 90)
        order_date = start_date + timedelta(days=random_days)
        
        order = {
            'id_food_order': i + 2,  # 从2开始,因为1已经被使用
            'order_nr': f'TEST{str(i+2).zfill(4)}',  # 生成类似 TEST0002 的订单号
            'restaurant_latitude': round(random.uniform(*lat_range), 6),  # 随机纬度,保留6位小数
            'restaurant_longitude': round(random.uniform(*lng_range), 6),  # 随机经度,保留6位小数
            'placed_at': order_date.strftime('%Y-%m-%d')
        }
        orders.append(order)
    
    return orders

# 生成数据
test_orders = generate_test_orders()

# 转换为JSON字符串并打印前5条和最后5条记录作为示例
print("前5条记录:")
print(json.dumps(test_orders[:5], indent=2, ensure_ascii=False))
print("\n最后5条记录:")
print(json.dumps(test_orders[-5:], indent=2, ensure_ascii=False))

# 输出完整数据
print("\n完整数据:")
print(json.dumps(test_orders, indent=2, ensure_ascii=False))