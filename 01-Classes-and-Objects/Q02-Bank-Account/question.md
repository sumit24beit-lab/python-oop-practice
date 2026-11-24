# Q02 — Customer Bank Account Management

**Difficulty:** Beginner  
**Concepts:** Classes, objects, constructors, instance attributes, object-state modification, methods, and validation

## Real-world scenario

A basic banking system needs to keep track of each customer's account balance and support deposits and withdrawals.

## Problem statement

Create a Python class named `BankAccount` to represent an individual customer's bank account.

### Attributes

| Attribute | Description |
|---|---|
| `account_number` | Unique bank account number |
| `customer_name` | Account holder's name |
| `balance` | Current available balance |

### Methods

- `deposit(amount)` — adds a valid deposit to the account balance.
- `withdraw(amount)` — subtracts a valid withdrawal when sufficient funds are available.
- `display_balance()` — displays the current balance.
- `display_details()` — displays the account information.

### Requirements

1. Create at least two account objects with different customer information and initial balances.
2. Display each account's details.
3. Perform a deposit and a withdrawal on each account.
4. Reject deposits and withdrawals of zero or negative amounts.
5. Reject a withdrawal that exceeds the available balance.
6. Do not modify the balance when a transaction is invalid.
7. Do not create a new account object for each transaction; update the existing object's state.

## Sample data and transactions

| Account | Customer | Initial balance | Deposit | Withdrawal |
|---|---|---:|---:|---:|
| 1001 | Amit | ₹10,000 | ₹5,000 | ₹3,000 |
| 1002 | Priya | ₹8,000 | ₹2,000 | ₹12,000 |

## Expected final balances

- Amit (1001): ₹12,000 after both valid transactions.
- Priya (1002): ₹10,000; the ₹12,000 withdrawal is rejected because the available balance is insufficient.

## Additional test cases

- Deposit ₹0 or a negative amount.
- Withdraw ₹0 or a negative amount.
- Withdraw more than the available balance.
- Verify that the balance remains unchanged after each rejected transaction.

## Learning objective

Practise modifying an object's existing state through its methods and validating operations before changing that state.
