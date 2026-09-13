# Day 54 - Database & ORM

## Overview

Day 54 of my 60-Day Data Science Challenge focused on database abstraction and Object-Relational Mapping (ORM) using Flask-SQLAlchemy.

I upgraded the modular Student Management REST API from Day 53 by replacing raw SQLite database operations with SQLAlchemy ORM models, relationships, and queries.

## Learning Objectives

- Understand Object-Relational Mapping
- Understand SQLAlchemy
- Configure Flask-SQLAlchemy
- Create database models
- Define columns and constraints
- Use primary keys
- Use foreign keys
- Implement one-to-many relationships
- Perform CRUD operations using ORM
- Query and filter database records
- Use database sessions
- Handle transactions
- Understand serialization
- Understand database migrations conceptually
- Integrate ORM with Flask REST APIs

## Major Project

### ORM-Based Student Management REST API

A modular Flask REST API that uses SQLAlchemy ORM for database operations.

The application supports user authentication, token-based API access, role-based authorization, and user-specific student management.

## Features

- User registration
- Secure password hashing
- User login
- Bearer token authentication
- Token expiration
- Token revocation
- Current user endpoint
- Student CRUD operations
- Multi-user data isolation
- Role-based authorization
- Admin statistics
- SQLAlchemy ORM
- Database relationships
- Input validation
- Centralized JSON responses
- Error handling
- Postman testing

## Database Models

### User

Fields:

- id
- username
- password
- role

### Student

Fields:

- id
- name
- age
- marks
- user_id

### Token

Fields:

- id
- token
- user_id
- expires_at

## Database Relationship

```text
User
 |
 | 1
 |
 | many
 ↓
Student

```text
Database Table  →  Python Model/Class
Database Row    →  Python Object
Database Column →  Object Attribute
