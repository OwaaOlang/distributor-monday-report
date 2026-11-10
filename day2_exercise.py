import sqlite3
import pandas as pd

conn = sqlite3.connect('distributor.db')

# (1) JOIN - each order with its customer's tier
q1 = """
SELECT
    o.order_id,
    o.customer_name,
    o.county AS order_county,
    c.account_tier,
    o.product,
    o.quantity * o.unit_price AS order_total
FROM orders o
JOIN customers c ON c.customer = o.customer_name
ORDER BY o.order_id
"""

# (2) Total spend per customer, only > 3 orders
q2 = """
SELECT
    o.customer_name,
    c.county,
    c.account_tier,
    COUNT(o.order_id) AS order_count,
    SUM(o.quantity * o.unit_price) AS total_spend
FROM orders o
JOIN customers c ON c.customer = o.customer_name
GROUP BY o.customer_name, c.county, c.account_tier
HAVING COUNT(o.order_id) > 3
ORDER BY total_spend DESC
"""

# (3) Top customer per county - window function
q3 = """
SELECT county, customer_name, total_spend FROM (
    SELECT
        c.county,
        o.customer_name,
        SUM(o.quantity * o.unit_price) AS total_spend,
        ROW_NUMBER() OVER (
            PARTITION BY c.county
            ORDER BY SUM(o.quantity * o.unit_price) DESC
        ) AS rn
    FROM orders o
    JOIN customers c ON c.customer = o.customer_name
    GROUP BY c.county, o.customer_name
)
WHERE rn = 1
ORDER BY total_spend DESC
"""

for i, q in enumerate([q1, q2, q3], 1):
    print(f"\n--- Query {i} ---")
    df = pd.read_sql_query(q, conn)
    print(df.to_string(index=False))
    print(f"Rows: {len(df)}")

conn.close()