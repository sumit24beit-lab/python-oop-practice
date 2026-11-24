# Q01 — Product Inventory Management

**Difficulty:** Beginner  
**Concepts:** Classes, objects, constructors, instance attributes, `self`, and instance methods

## Real-world scenario

A local grocery store needs a simple way to maintain product information and calculate the monetary value of its available stock.

## Problem statement

Create a Python class named `Product` to represent an individual product.

### Attributes

| Attribute | Description |
|---|---|
| `product_id` | Unique product identification number |
| `product_name` | Product name |
| `price` | Price per unit |
| `quantity` | Available stock quantity |

### Methods

- `display_details()` — displays all product information.
- `calculate_stock_value()` — returns the total value of the available stock (`price × quantity`).

### Requirements

1. Create at least three product objects with different information.
2. Display the details of each product.
3. Calculate the stock value through the class method; do not hardcode the results.
4. Use the same class to create all objects.

## Sample data

| Product ID | Product name | Price | Quantity |
|---|---|---:|---:|
| P101 | Rice | ₹60 | 50 |
| P102 | Wheat | ₹40 | 30 |
| P103 | Sugar | ₹45 | 20 |

## Expected stock values

| Product | Calculation | Stock value |
|---|---:|---:|
| Rice | 60 × 50 | ₹3,000 |
| Wheat | 40 × 30 | ₹1,200 |
| Sugar | 45 × 20 | ₹900 |

## Learning objective

Practise defining a class, creating multiple independent objects, initializing instance attributes, and calling methods through objects.
