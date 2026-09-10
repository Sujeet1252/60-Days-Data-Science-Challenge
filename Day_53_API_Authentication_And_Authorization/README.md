# Day 53 - API Authentication & Authorization

## 📌 Overview

Day 53 of my 60-Day Data Science Challenge focused on **API Authentication & Authorization using Flask and JWT**.

In this project, I upgraded the modular Flask REST API from Day 52 by implementing secure API authentication using **JSON Web Tokens (JWT)** and role-based authorization.

The application supports different user roles and controls which API operations each role is allowed to perform.

---

## 🎯 Learning Objectives

During Day 53, I learned:

- Authentication vs Authorization
- API security fundamentals
- Token-based authentication
- JSON Web Tokens (JWT)
- JWT Header, Payload and Signature
- Access Tokens
- Bearer Token Authentication
- Protecting Flask API endpoints
- `jwt_required()`
- `get_jwt_identity()`
- `get_jwt()`
- Role-Based Access Control
- User roles and permissions
- HTTP 401 Unauthorized
- HTTP 403 Forbidden
- Testing authenticated APIs using Postman
- Protecting application secrets
- Using `.env` for sensitive configuration

---

## 🔐 Authentication vs Authorization

### Authentication

Authentication verifies the identity of a user.

**Question:**

> Who are you?

Example:

```text
Username + Password
        ↓
Server verifies credentials
        ↓
User authenticated
