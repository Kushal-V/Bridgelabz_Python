import json

class Product:
    def __init__(self,product_id,name,price,quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def to_dict(self):
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }

class Cart:
    def __init__(self,cart_id):
        self.cart_id = cart_id
        self.products = []
    
    def add_product(self,product):
        self.products.append(product)
    
    def to_json(self):
        cart_data = {
            'cart_id': self.cart_id,
            'products': [product.to_dict() for product in self.products],
            'total_amount': sum(product.price * product.quantity for product in self.products)
        }
        return json.dumps(cart_data)

p1 = Product(1, "Laptop", 50000, 1)
p2 = Product(2, "Mouse", 500, 2)

cart = Cart("CART123")
cart.add_product(p1)
cart.add_product(p2)

print(cart.to_json())