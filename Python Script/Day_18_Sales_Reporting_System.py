#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

conn = sqlite3.connect("SalesReporting.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers(
    CustomerID INTEGER PRIMARY KEY,
    CustomerName TEXT,
    City TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders(
    OrderID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    Amount INTEGER
)
""")

cursor.execute("DELETE FROM Customers")
cursor.execute("DELETE FROM Orders")

customers = [
    (1, "Rahul", "Delhi"),
    (2, "Priya", "Mumbai"),
    (3, "Aman", "Lucknow"),
    (4, "Neha", "Delhi"),
    (5, "Rohit", "Pune")
]

orders = [
    (101, 1, 5000),
    (102, 2, 8000),
    (103, 1, 3000),
    (104, 3, 10000),
    (105, 2, 7000),
    (106, 4, 4000),
    (107, 5, 6000)
]

cursor.executemany(
    "INSERT INTO Customers VALUES(?,?,?)",
    customers
)

cursor.executemany(
    "INSERT INTO Orders VALUES(?,?,?)",
    orders
)

conn.commit()

print("\nTOTAL ORDERS")
cursor.execute("""
SELECT COUNT(*)
FROM Orders
""")
print(cursor.fetchone()[0])

print("\nTOTAL REVENUE")
cursor.execute("""
SELECT SUM(Amount)
FROM Orders
""")
print(cursor.fetchone()[0])

print("\nAVERAGE REVENUE")
cursor.execute("""
SELECT AVG(Amount)
FROM Orders
""")
print(round(cursor.fetchone()[0], 2))

print("\nTOP CUSTOMER ORDER")
cursor.execute("""
SELECT *
FROM Orders
ORDER BY Amount DESC
LIMIT 1
""")
print(cursor.fetchone())

print("\nCUSTOMER-WISE REVENUE")
cursor.execute("""
SELECT CustomerID,
       SUM(Amount)
FROM Orders
GROUP BY CustomerID
""")

for row in cursor.fetchall():
    print(row)

conn.close()


# In[ ]:




