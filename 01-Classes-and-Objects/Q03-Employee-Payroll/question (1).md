# Q03 — Employee Payroll Management

**Difficulty:** Beginner  
**Concepts:** Classes, objects, constructors, instance attributes, instance methods, method reuse, and calculations

## Real-world scenario

A company's HR department needs a simple way to calculate monthly employee salaries from basic salary, allowances, and a deduction.

## Problem statement

Create a Python class named `Employee` to represent an employee and calculate their monthly net salary.

### Attributes

| Attribute | Description |
|---|---|
| `employee_id` | Unique employee identification number |
| `employee_name` | Employee's full name |
| `basic_salary` | Employee's basic monthly salary |

### Methods

- `calculate_hra()` — calculates HRA as 20% of basic salary.
- `calculate_da()` — calculates DA as 10% of basic salary.
- `calculate_pf()` — calculates PF as 12% of basic salary.
- `calculate_net_salary()` — calculates the final net salary.
- `display_pay_slip()` — displays the complete salary breakdown.

### Formula

`Net Salary = Basic Salary + HRA + DA - PF`

For this exercise, the percentages are simplified educational assumptions, not a complete real-world payroll or statutory tax calculation.

### Requirements

1. Create at least three employee objects with different employee information and basic salaries.
2. Calculate each salary component using its own method.
3. Reuse the component methods inside `calculate_net_salary()`.
4. Display each employee's complete pay slip.
5. Do not hardcode the calculated amounts.

## Sample data

| Employee ID | Employee name | Basic salary |
|---|---|---:|
| E101 | Amit Sharma | ₹30,000 |
| E102 | Priya Patil | ₹45,000 |
| E103 | Rahul Verma | ₹60,000 |

## Expected results

| Employee | HRA (20%) | DA (10%) | PF (12%) | Net salary |
|---|---:|---:|---:|---:|
| Amit Sharma | ₹6,000 | ₹3,000 | ₹3,600 | ₹35,400 |
| Priya Patil | ₹9,000 | ₹4,500 | ₹5,400 | ₹53,100 |
| Rahul Verma | ₹12,000 | ₹6,000 | ₹7,200 | ₹70,800 |

## Learning objective

Practise dividing a larger calculation into smaller reusable methods and calling those methods from another method of the same object.
