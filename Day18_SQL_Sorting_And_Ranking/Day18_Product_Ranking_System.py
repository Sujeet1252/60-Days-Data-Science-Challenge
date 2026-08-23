#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

# Connect Database
conn = sqlite3.connect("ProductRanking.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Product(
    product_name TEXT,
    category TEXT,
    price INTEGER
)
""")

# Clear Old Data (Optional)
cursor.execute("DELETE FROM Product")

# Insert Data
products = [
    ("Laptop", "Electronics", 65000),
    ("Mobile", "Electronics", 30000),
    ("Headphones", "Electronics", 2500),
    ("TV", "Electronics", 55000),
    ("Washing Machine", "Home Appliance", 40000),
    ("Refrigerator", "Home Appliance", 45000),
    ("Keyboard", "Accessories", 1200),
    ("Mouse", "Accessories", 800),
    ("Smart Watch", "Electronics", 8000),
    ("Printer", "Office", 15000)
]

cursor.executemany(
    "INSERT INTO Product VALUES(?,?,?)",
    products
)

conn.commit()

print("="*50)
print("MOST EXPENSIVE PRODUCT")
print("="*50)

cursor.execute("""
SELECT *
FROM Product
ORDER BY Price DESC
LIMIT 1;
""")

for row in cursor.fetchall():
    print(row)

print("\n" + "="*50)
print("CHEAPEST PRODUCT")
print("="*50)

cursor.execute("""
SELECT *
FROM Product
ORDER BY Price ASC
LIMIT 1;
""")

for row in cursor.fetchall():
    print(row)

print("\n" + "="*50)
print("TOP 3 PRODUCTS")
print("="*50)

cursor.execute("""
SELECT *
FROM Product
ORDER BY Price DESC
LIMIT 3;
""")

for row in cursor.fetchall():
    print(row)

print("\n" + "="*50)
print("TOP 5 PRODUCTS")
print("="*50)

cursor.execute("""
SELECT *
FROM Product
ORDER BY Price DESC
LIMIT 5;
""")

for row in cursor.fetchall():
    print(row)

print("\n" + "="*50)
print("PRICE ASCENDING")
print("="*50)

cursor.execute("""
SELECT *
FROM Product
ORDER BY Price ASC;
""")

for row in cursor.fetchall():
    print(row)

print("\n" + "="*50)
print("PRICE DESCENDING")
print("="*50)

cursor.execute("""
SELECT *
FROM Product
ORDER BY Price DESC;
""")

for row in cursor.fetchall():
    print(row)

conn.close()

