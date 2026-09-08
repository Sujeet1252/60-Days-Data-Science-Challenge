# Day 52 — Advanced Flask API Integration

## 📌 Overview

Day 52 focuses on improving Flask REST APIs with professional API design concepts.

The project extends the Multi-User Student Management REST API developed in Day 51.

## 🎯 Objectives

- Understand advanced REST API concepts
- Implement request validation
- Use query parameters
- Implement search functionality
- Implement filtering
- Implement pagination
- Understand HTTP status codes
- Create consistent JSON responses
- Implement API error handling
- Improve API reliability and usability

## 🛠️ Technologies Used

- Python
- Flask
- SQLite
- REST API
- JSON
- Postman
- Werkzeug

## 🔑 Features

### Authentication

- User registration
- User login
- Flask session authentication
- Protected API endpoints

### Student API

- Create student
- Read students
- Update student
- Delete student

### Advanced API Features

- Search students by name
- Filter students by marks
- Combine multiple filters
- Pagination
- Request validation
- Error handling
- Proper HTTP status codes
- Consistent JSON responses

## 🔗 API Examples

### Get Students

GET `/api/students`

### Search

GET `/api/students?search=Rahul`

### Filter

GET `/api/students?min_marks=70`

### Search + Filter

GET `/api/students?search=Rahul&min_marks=70`

### Pagination

GET `/api/students?page=1&limit=10`

## 📊 HTTP Status Codes

| Status Code | Meaning |
|-------------|---------|
| 200 | Successful request |
| 201 | Resource created |
| 400 | Bad request |
| 401 | Authentication required |
| 403 | Forbidden |
| 404 | Resource not found |
| 409 | Conflict |
| 500 | Internal server error |

## 🧠 Key Concepts Learned

- REST API architecture
- Query parameters
- Request validation
- JSON responses
- Pagination
- Filtering
- Searching
- HTTP status codes
- API error handling
- Authentication-aware APIs

## 📂 Project Structure

```text
Day_52_Advanced_Flask_API/
│
├── app.py
├── init_db.py
├── templates/
├── static/
├── screenshots/
├── .gitignore
└── README.md
