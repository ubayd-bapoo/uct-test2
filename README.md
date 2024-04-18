# Explanation of Changes:

## PaymentProcessor Interface:
* I introduced an abstract class PaymentProcessor as an interface for payment processors, defining the process_payment method.
* DebitCardProcessor, CreditCardProcessor, and PayPalProcessor are concrete implementations of PaymentProcessor.

## Low Coupling and High Cohesion:
* Each payment processor now handles its specific payment logic independently, promoting low coupling.
* Cohesion is increased as each class has a single responsibility related to processing its specific payment type.

## PayPal Payment Type:
* Added a new PayPalProcessor class that implements the PayPal payment type, requiring an email address instead of a security code.

## Order Class Improvement:
* Moved the payment processing logic (process_payment) to the Order class, allowing it to accept any payment processor implementing the PaymentProcessor interface.
* This separation of concerns improves the extensibility and maintainability of the codebase.

## Documentation:
* Comments and method docstrings are added to describe the purpose of each class and method, enhancing code readability and understanding.

This updated code adheres to SOLID principles, improves code structure, and introduces extensibility by enabling easy addition of new payment types.

# Competency Assessment

## Introduction
The purpose of this task is to evaluate your ability to produce readable and efficient code that is easily extensible. Your ability to incorporate design principles into your code is key.

### Task
This repository contains the code for a python script that processes a fictitious order. You are expected to read the code and gain an understanding of what the application does.

Your are required to:

1. Use SOLID design principles to update the script so that there is low coupling and high cohesion, making the code easily extensible. (30)
2. Extend the application so that it can process a new payment type called "PayPal", that requires an email address instead of a security code. (10)
3. Ensure that your code is well documented. (10)