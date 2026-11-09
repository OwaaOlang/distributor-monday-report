


pricing for a distributor:
setup fee: KES 35,000 one-time - Build database, clean excel data, create 5 monday reports, train staff.
monthly support: KES 10,000 / month - fix errors, add new reports, monthly check-in, keep data backed up.



README
# Nairobi Wholesale Distributor - Monday Report

Replaces 45 minutes of manual Excel work with one Python + SQL script.

## What it does
Uses SQLite + pandas to answer the 5 questions the Sales Manager asks every Monday.

### Database: distributor.db
Table: `orders`
- order_id, customer_name, county, product, quantity, unit_price, order_date, status
- 22 realistic orders
- Total value is calculated as: `quantity * unit_price`

### 5 Questions Answered
1. All orders from Mombasa
2. Top 10 orders by total value
3. Total revenue per county
4. All pending orders over KES 50,000
5. Top 3 best-selling products by quantity

### Key Results
- Top county by revenue: Mombasa - KES 338,750
- Top product by value: Rice 25kg
- Top product by quantity: Maize Flour 2kg
- Urgent follow-ups: 3 pending orders over KES 50,000

## How to run
```bash
python today_exercise.py