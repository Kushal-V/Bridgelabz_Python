import json

def main():
    products = json.loads(input("Enter data: "))

    updated_products = {
        product_id: {
            **details,
            "price": (
                details["price"] * 0.85
                if details["price"] > 50 and details["category"] == "Electronics"
                else details["price"] * 0.95
                if details["price"] > 50 and details["category"] == "Fashion"
                else details["price"]
            )
        }
        for product_id, details in products.items()
    }

    [print(f"{product_id}: {details}") for product_id, details in updated_products.items()]

main()
