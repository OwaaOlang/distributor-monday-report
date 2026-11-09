import sqlite3
import pandas as pd

# 1. Create fresh DB
conn = sqlite3.connect("distributor.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS orders")
cur.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    county TEXT,
    product TEXT,
    quantity INTEGER,
    unit_price REAL,
    order_date TEXT,
    status TEXT
)
""")

# 2. Insert 20+ realistic rows
orders = [
    (1001, 'Kamau Stores', 'Nairobi', 'Maize Flour 2kg', 50, 120, '2026-11-02', 'delivered'),
    (1002, 'Otieno Shop', 'Kisumu', 'Cooking Oil 5L', 20, 1350, '2026-11-02', 'delivered'),
    (1003, 'Njoroge Supplies', 'Nakuru', 'Sugar 1kg', 100, 255, '2026-11-03', 'delivered'),
    (1004, 'Hassan Traders', 'Mombasa', 'Rice 25kg', 40, 3200, '2026-11-03', 'delivered'),
    (1005, 'Waweru Ltd', 'Nairobi', 'Maize Flour 2kg', 80, 120, '2026-11-03', 'pending'),
    (1006, 'Owino Retail', 'Kisumu', 'Sugar 1kg', 60, 250, '2026-11-04', 'delivered'),
    (1007, 'Karanja Wholesalers', 'Mombasa', 'Cooking Oil 5L', 30, 1350, '2026-11-04', 'pending'),
    (1008, 'Kiprono Stores', 'Eldoret', 'Rice 25kg', 15, 3200, '2026-11-04', 'delivered'),
    (1009, 'Ochieng Supplies', 'Kisumu', 'Maize Flour 2kg', 200, 240, '2026-11-05', 'delivered'),
    (1010, 'Mutua Enterprises', 'Machakos', 'Cooking Oil 5L', 25, 850, '2026-11-05', 'pending'),
    (1011, 'Ali Distributors', 'Mombasa', 'Sugar 1kg', 150, 255, '2026-11-05', 'delivered'),
    (1012, 'Chebet Shop', 'Eldoret', 'Maize Flour 2kg', 90, 120, '2026-11-06', 'delivered'),
    (1013, 'Muthoni Traders', 'Nairobi', 'Rice 25kg', 20, 3200, '2026-11-06', 'pending'),
    (1014, 'Baraka Stores', 'Mombasa', 'Rice 25kg', 30, 3200, '2026-11-06', 'pending'),
    (1015, 'Wanjiru Retail', 'Nakuru', 'Cooking Oil 5L', 18, 1350, '2026-11-07', 'delivered'),
    (1016, 'Kiprop Wholesalers', 'Eldoret', 'Sugar 1kg', 80, 255, '2026-11-07', 'delivered'),
    (1017, 'Achieng Shop', 'Kisumu', 'Rice 25kg', 12, 3200, '2026-11-07', 'pending'),
    (1018, 'Mwangi Stores', 'Nairobi', 'Sugar 1kg', 120, 255, '2026-11-08', 'delivered'),
    (1019, 'Juma Traders', 'Mombasa', 'Maize Flour 2kg', 300, 120, '2026-11-08', 'delivered'),
    (1020, 'Nyambura Ltd', 'Machakos', 'Rice 25kg', 18, 3200, '2026-11-08', 'pending'),
    (1021, 'Omondi Supplies', 'Kisumu', 'Cooking Oil 5L', 40, 1350, '2026-11-09', 'delivered'),
    (1022, 'Kibet Stores', 'Nakuru', 'Maize Flour 2kg', 70, 120, '2026-11-09', 'pending'),
]
cur.executemany("INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?, ?, ?)", orders)
conn.commit()

def ask(title, query):
    print(f"\n=== {title} ===")
    df = pd.read_sql_query(query, conn)
    print(df.to_string(index=False))

# (1) All orders from Mombasa
ask("1. All orders from Mombasa", 
    "SELECT * FROM orders WHERE county = 'Mombasa'")

# (2) Top 10 orders by total value
ask("2. Top 10 orders by total value",
    "SELECT order_id, customer_name, county, product, quantity, unit_price, quantity * unit_price AS total_value FROM orders ORDER BY total_value DESC LIMIT 10")

# (3) Total revenue per county
ask("3. Total revenue per county",
    "SELECT county, COUNT(*) AS orders, SUM(quantity * unit_price) AS total_revenue FROM orders GROUP BY county ORDER BY total_revenue DESC")

# (4) All pending orders over KES 50,000
ask("4. Pending orders over KES 50,000",
    "SELECT order_id, customer_name, county, product, quantity * unit_price AS total_value, status FROM orders WHERE status = 'pending' AND quantity * unit_price > 50000 ORDER BY total_value DESC")

# (5) Three best-selling products by quantity
ask("5. Top 3 best-selling products by quantity",
    "SELECT product, SUM(quantity) AS total_quantity, SUM(quantity * unit_price) AS total_revenue FROM orders GROUP BY product ORDER BY total_quantity DESC LIMIT 3")

conn.close()