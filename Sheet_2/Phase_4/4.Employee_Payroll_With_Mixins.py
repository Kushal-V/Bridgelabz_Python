class TaxMixin:
    def calculate_tax(self):
        return self.salary * 0.1

class SalaryEmployee(TaxMixin):
    def __init__(self, salary):
        self.salary = salary
    
    def calculate_pay(self):
        return self.salary - self.calculate_tax()
        

class CommisionEmployee(TaxMixin):
    def __init__(self, salary,commission):
        self.salary = salary
        self.commission = commission
    
    def calculate_pay(self):
        total_pay = self.salary + self.commission
        return total_pay - self.calculate_tax()

emp1 = SalaryEmployee(1000)
emp2 = CommisionEmployee(1000,100)
print(emp1.calculate_pay())
print(emp2.calculate_pay())
