# FastAPI Blog Management System (Training Project) 🚀

A professional RESTful API built with **FastAPI**. This project was developed as a comprehensive training journey to master modern backend development with Python, following the best practices for clean architecture, security, and the **Repository Pattern**.

## 🌟 Overview

This is a full-featured Blog Management System where users can register, authenticate, and manage blog posts. The project demonstrates a clear separation of concerns by isolating business logic from database operations, making the codebase scalable and maintainable.

## 🛠️ Tech Stack

- **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Database/ORM:** SQLAlchemy (SQLite by default)
- **Data Validation:** Pydantic Models
- **Security:** JWT (JSON Web Tokens) & OAuth2
- **Password Hashing:** Passlib with BCrypt
- **Environment:** Python 3.x

## 🎓 Skills & Concepts Implemented

Based on a comprehensive 4-hour intensive FastAPI curriculum, I have successfully implemented:

- **API Fundamentals:** Handling Path & Query parameters, Request Bodies, and custom HTTP Status Codes.
- **Database Management:** Full CRUD operations (Create, Read, Update, Delete) using SQLAlchemy ORM.
- **Data Validation & Transformation:** Using Pydantic Schemas for strict request validation and specialized Response Models.
- **System Architecture:** \* Implementation of the **Repository Pattern**.
  - Modularizing the application using **APIRouter** for clean code organization.
- **Security & Authentication:** \* Secure password hashing using BCrypt.
  - Logic for Login and Identity Verification.
  - JWT Access Token generation and verification.
  - Protecting routes using Authentication dependencies (OAuth2).
- **Advanced Features:** \* Establishing **Relationships** (One-to-Many) between Users and Blogs.
  - Professional Error Handling with custom HTTP Exceptions.
- **Documentation:** Interactive API documentation via Swagger UI and ReDoc.

## 📁 Project Structure

```text
app/
├── main.py            # Entry point of the application
├── database.py        # Database connection & Session configuration
├── models.py          # SQLAlchemy Database models
├── schemas.py         # Pydantic schemas for Data Validation
├── hashing.py         # Password encryption logic (Utility)
├── oauth2.py          # Authentication dependency & Route protection
├── JWTtoken.py        # JWT generation and verification logic
├── routers/           # Modular API route handlers (Blogs, Users, Auth)
└── repository/        # Business logic & DB queries (Repository Pattern)
```

## Acknowledgements

This project marks the completion of a deep-dive training into FastAPI, covering everything from basic routing to advanced JWT security and deployment readiness

## 🚀 Getting Started

**Clone the repository:**

```bash
git clone [https://github.com/Mithgal-JH/FastAPI_Training_Project.git]
(https://github.com/Mithgal-JH/FastAPI_Training_Project.git)
cd FastAPI_Training_Project
```
