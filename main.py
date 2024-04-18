from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    """Abstract base class for payment processors."""

    @abstractmethod
    def process_payment(self) -> None:
        """Process payment for the order."""
        pass


class DebitCardProcessor(PaymentProcessor):
    """Payment processor for debit card payments."""

    def __init__(self, security_code: str) -> None:
        """Initialize DebitCardProcessor.

        Args:
            security_code (str): The security code for the debit card.
        """
        self.security_code = security_code

    def process_payment(self) -> None:
        """Process payment using a debit card."""
        print(f"Processing debit card payment type...")
        print(f"Verifying security code {self.security_code}")
        self.complete_payment()

    def complete_payment(self) -> None:
        """Complete the payment process."""
        print("Payment completed.")
        self.status = "paid"


class CreditCardProcessor(PaymentProcessor):
    """Payment processor for credit card payments."""

    def __init__(self, security_code: str) -> None:
        """Initialize CreditCardProcessor.

        Args:
            security_code (str): The security code for the credit card.
        """
        self.security_code = security_code

    def process_payment(self) -> None:
        """Process payment using a credit card."""
        print(f"Processing credit card payment type...")
        print(f"Verifying security code {self.security_code}")
        self.complete_payment()

    def complete_payment(self) -> None:
        """Complete the payment process."""
        print("Payment completed.")
        self.status = "paid"


class PayPalProcessor(PaymentProcessor):
    """Payment processor for PayPal payments."""
    def __init__(self, email: str) -> None:
        """Initialize PayPalProcessor.

        Args:
            email (str): The email address associated with the PayPal account.
        """
        self.email = email

    def process_payment(self) -> None:
        """Process payment using PayPal."""
        print(f"Processing PayPal payment type...")
        print(f"Verifying email address {self.email}")
        self.complete_payment()

    def complete_payment(self) -> None:
        """Complete the payment process."""
        print("Payment completed.")
        self.status = "paid"


class Order:
    """Represents an order with items to be purchased."""

    def __init__(self) -> None:
        """Initialize Order."""
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name: str, quantity: int, price: float) -> None:
        """Add an item to the shopping cart.

        Args:
            name (str): The name of the item.
            quantity (int): The quantity of the item.
            price (float): The price of the item.
        """
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self) -> float:
        """Calculate the total cost for all items and their quantities.

        Returns:
            float: The total cost of the order.
        """
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

    def process_payment(self, payment_processor: PaymentProcessor) -> None:
        """Process payment for the order using the given payment processor.

        Args:
            payment_processor (PaymentProcessor): The payment processor to use.
        """
        payment_processor.process_payment()
        self.status = "paid"


if __name__ == "__main__":
    order = Order()
    order.add_item("Keyboard", 1, 250.50)
    order.add_item("Mouse", 1, 150.00)
    order.add_item("Monitor", 1, 3500.00)

    print(f"Total amount: {order.total_price()}")

    debit_processor = DebitCardProcessor("abcd12345")
    order.process_payment(debit_processor)

    paypal_processor = PayPalProcessor("example@example.com")
    order.process_payment(paypal_processor)
