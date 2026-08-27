# Day 51 - Authenticated REST API with Flask

## 📌 Overview

Day 51 focuses on integrating Flask authentication with REST APIs and SQLite.

The project combines the concepts learned during Days 48, 49, and 50 to create a multi-user Student Management REST API.

Each authenticated user can manage their own student records through protected API endpoints.

---

## 🎯 Learning Objectives

- Integrate authentication with REST APIs
- Create protected API endpoints
- Understand HTTP 401 and 403
- Use Flask sessions
- Associate database records with users
- Implement user-specific data access
- Build authenticated CRUD APIs
- Validate API input
- Test protected APIs using Postman

---

## 📚 Topics Covered

### Authentication

Authentication verifies the identity of a user.

### Authorization

Authorization determines whether an authenticated user is allowed to access a resource.

### Protected API

An API endpoint that requires authentication before allowing access.

### User-Specific Data

Each student record is associated with the user who created it.

```text
User
 ↓
user_id
 ↓
Student Records
