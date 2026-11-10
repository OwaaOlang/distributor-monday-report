


## Pricing for a Distributor

**Setup fee: KES 35,000 one-time**
- Build database
- Clean Excel data
- Create 5 Monday reports
- Train staff

**Monthly support: KES 10,000 / month**
- Fix errors
- Add new reports
- Monthly check-in
- Keep data backed up

Why separate? Setup is building it once. Support is keeping it running.



README
# Nairobi Wholesale Distributor - Monday Report

![Monday Report Output](output.png)

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




# Nairobi Distributor - Who Drives Revenue?

## Query 1: Orders + Account Tier
**Answers:** For each order, is this a gold / silver / bronze customer?
**Why a sales manager cares:** Stop treating all orders the same. Gold orders get priority stock and faster delivery.

## Query 2: Total Spend per Customer (>3 orders)
**Answers:** Who are the repeat, high-value customers?
**Why a sales manager cares:** These are your retention list. Losing one of these hurts more than losing 10 one-time buyers.

## Query 3: Top Customer per County
**Answers:** Who is #1 in Nairobi, Mombasa, Kisumu, etc?
**Why a sales manager cares:** Shows if revenue is concentrated in one county. If Mombasa is all Hassan Traders, that's a risk - and an opportunity to grow other counties.

## Pricing Note
This level of SQL reporting work: UGX 150,000 - 300,000 per report / dashboard for a small distributor.
