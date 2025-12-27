import json

data = input("Enter the data: ")
items = json.loads(data)

alert_items = list(
    map(lambda item: f"{item['name']} is low in stock", filter(lambda item: item['stock'] < item['reorder_level'], items))
)

print(alert_items)
