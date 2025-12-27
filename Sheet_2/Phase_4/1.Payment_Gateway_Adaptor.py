from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount):
        pass


class Stripe:
    def charge_card(self, amount):
        print(f"Stripe charged {amount}")


class Paypal:
    def make_payment(self, amount):
        print(f"PayPal paid {amount}")


class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe):
        self.stripe = stripe

    def process(self, amount):
        self.stripe.charge_card(amount)


class PaypalAdapter(PaymentProcessor):
    def __init__(self, paypal):
        self.paypal = paypal

    def process(self, amount):
        self.paypal.make_payment(amount)


def checkout(processor: PaymentProcessor, amount):
    processor.process(amount)


stripe = Stripe()
paypal = Paypal()

checkout(StripeAdapter(stripe), 100)
checkout(PaypalAdapter(paypal), 200)
