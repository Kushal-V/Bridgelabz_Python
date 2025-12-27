class Restaurant:
    def __init__(self):
        self.menu = {
            "Pizza": {"Price": 100, "Prep_time": 10},
            "Burger": {"Price": 50, "Prep_time": 5},
            "Pasta": {"Price": 75, "Prep_time": 8}
        }
        self.orders = []
    
    def order(self,items):
        total_price = 0
        prep_time = []
        for item in items:
            if item in self.menu:
                total_price += self.menu[item]["Price"]
                prep_time.append(self.menu[item]["Prep_time"])
            else:
                print(f"{item} is not available")
                return
        
        max_time = max(prep_time)

        order = {"items": items, "total_price": total_price, "max_time": max_time}
        self.orders.append(order)
        print(f"Order placed successfully. Total price: {total_price}")
        print(f"Order will be ready in {max_time} minutes")

order1 = Restaurant()
order1.order(["Pizza", "Burger"])

