# Student Management System API

## Overview

The Student Management System API is a Python-based REST API built using **FastAPI** and **SQLite**. It provides basic functionality to manage student records, including adding new students, listing all students, and deleting students.

The project demonstrates the fundamentals of REST API development, database connectivity, and CRUD operations.

## Features

- **Add Student:** Register a new student with their name and email address.
- **List Students:** Retrieve all registered student records.
- **Delete Student:** Remove a student record using their unique ID.
- **Database Integration:** Store student information in an SQLite database.
- **Duplicate Prevention:** Prevent multiple student records from using the same email address.
- **Interactive API Documentation:** Test API endpoints using FastAPI's Swagger UI.

## Technologies Used

- Python
- FastAPI
- SQLite
- Uvicorn
- Pydantic

## Project Structure

```text
student-management-system/
├── main.py
├── db.py
├── users.db
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd student-management-system
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn
```

### 4. Initialize the Database

```bash
python db.py
```

This creates the SQLite database and the table used to store student records.

### 5. Start the API Server

```bash
uvicorn main:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/users` | Add a new student |
| GET | `/users` | Retrieve all students |
| DELETE | `/users/{user_id}` | Delete a student by ID |

## Example Request

### Add a Student

**Endpoint:** `POST /users`

Request body:

```json
{
  "name": "Rahul Sharma",
  "email": "rahul@example.com"
}
```

Example response:

```json
{
  "message": "User added successfully",
  "user": {
    "id": 1,
    "name": "Rahul Sharma",
    "email": "rahul@example.com"
  }
}
```

### List Students

**Endpoint:** `GET /users`

Returns the total number of students and their records.

### Delete a Student

**Endpoint:** `DELETE /users/1`

Deletes the student whose ID is `1`.

## API Documentation

Once the server is running, open the following URL in your browser to explore and test the API endpoints:

**Swagger UI:** http://127.0.0.1:8000/docs

**ReDoc:** http://127.0.0.1:8000/redoc

## Database

The project uses SQLite to persist student records in a local database file named `users.db`.

Each student record contains:

- `id`: Unique student identifier.
- `name`: Student's name.
- `email`: Student's unique email address.

## Future Enhancements

- Update student details.
- Add student roll numbers, courses, and department information.
- Implement search and filtering.
- Add authentication and authorization.
- Introduce pagination for student listings.
- Migrate to PostgreSQL for larger applications.

## License

This project is intended for educational and learning purposes.
