# Day 50 - Flask User Authentication

## 📌 Overview

Day 50 focuses on implementing user authentication using Flask and SQLite.

The project includes user registration, secure password hashing, login, sessions, protected routes, and logout functionality.

---

## 🎯 Learning Objectives

- Understand authentication
- Understand authorization
- Learn user registration
- Learn user login
- Learn password hashing
- Learn Flask sessions
- Create protected routes
- Implement logout
- Connect authentication with SQLite
- Handle duplicate usernames
- Understand basic authentication security

---

## 📚 Topics Covered

### Authentication

Authentication verifies the identity of a user.

### Authorization

Authorization determines what an authenticated user is allowed to access.

### Password Hashing

Passwords are stored as hashes instead of plain text.

Flask uses Werkzeug security utilities:

```python
generate_password_hash()
check_password_hash()
