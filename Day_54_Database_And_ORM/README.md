# Day 54 - Database & ORM

## 📌 Overview

Day 54 of my 60-Day Data Science Challenge focused on **Database Management and Object-Relational Mapping (ORM)** using Flask and SQLAlchemy.

I upgraded the previous Flask REST API by replacing direct database operations with a more structured ORM-based database architecture.

The project uses **Flask-SQLAlchemy** with SQLite and integrates database models with the existing JWT authentication and role-based authorization system.

---

## 🎯 Learning Objectives

During Day 54, I learned:

- Database fundamentals
- SQL and database operations
- Object-Relational Mapping (ORM)
- SQLAlchemy
- Flask-SQLAlchemy
- Database Models
- Tables and Rows
- Columns and Attributes
- Primary Keys
- Foreign Keys
- One-to-Many Relationships
- CRUD operations using ORM
- Database Sessions
- `db.session.add()`
- `db.session.commit()`
- `db.session.delete()`
- Querying with SQLAlchemy
- Connecting Flask with a database using ORM

---

## 🧠 What is ORM?

ORM stands for **Object-Relational Mapping**.

ORM allows developers to work with database records using programming-language objects and classes instead of writing SQL queries for every operation.

The basic mapping is:

```text
Database Table  →  Python Model/Class
Database Row    →  Python Object
Database Column →  Object Attribute
