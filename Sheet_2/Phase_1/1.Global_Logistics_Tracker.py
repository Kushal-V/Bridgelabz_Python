import json

def main():
    ships = json.loads(input("Enter data: "))

    result = [
        item["name"]
        for ship in ships
        for container in ship["containers"]
        for item in container["items"]
        if item["type"] == "Fragile"
        and item["destination"] == "LON"
        and item["weight"] > 10
    ]

    print(result)

main()
