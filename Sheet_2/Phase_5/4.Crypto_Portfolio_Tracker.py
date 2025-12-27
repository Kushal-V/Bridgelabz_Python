import json

portfolio_data = json.loads(input("Enter Portfolio Data: "))
price_data = json.loads(input("Enter Current Prices Data: "))

class Portfolio:
    def __init__(self,portfolio,prices):
        self.portfolio = portfolio
        self.prices = prices
    
    @property
    def total_value_usd(self):
        return sum(quantity * self.prices.get(asset,0) for asset, quantity in self.portfolio.items())

p = Portfolio(portfolio_data,price_data)
print(p.total_value_usd)