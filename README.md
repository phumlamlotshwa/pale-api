# Palé Builder Challenge — Simple API with Authentication & Database Access

A RESTful API built with FastAPI, featuring JWT authentication, bcrypt password hashing, and SQLite database access. Built as part of the Palé Cloud & Platform Engineering Internship application.

---

## Tech Stack

- **Python** — core language
- **FastAPI** — web framework
- **SQLite** — database
- **SQLAlchemy** — ORM for database access
- **JWT (JSON Web Tokens)** — authentication
- **bcrypt** — password hashing
- **Passlib** — password utilities

---

## How It Works

### Architecture
```
Client → FastAPI Router → Auth Middleware → Database (SQLite)
```

- User registers with a username, email and password
- Password is **hashed with bcrypt** before storing in the database — plain text passwords are never saved
- User logs in and receives a **JWT access token**
- Protected routes require a valid token in the request header — requests without a token receive a **401 Unauthorized** response

---

## Endpoints

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| GET | `/` | No | Health check |
| POST | `/auth/register` | No | Register a new user |
| POST | `/auth/login` | No | Login and receive JWT token |
| GET | `/user/profile` | ✅ Yes | Access protected user data |

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/pale-api.git
cd pale-api
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root folder:
```env
DATABASE_URL=sqlite:///./pale_api.db
SECRET_KEY=your-super-secret-key-change-this
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Run the server
```bash
uvicorn main:app --reload
```

### 6. Open API docs
Visit **http://127.0.0.1:8000/docs** to explore and test all endpoints interactively.

---

## Testing the API

### Register a user
```bash
curl -X POST "http://127.0.0.1:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "test@example.com", "password": "testpassword123"}'
```

### Login
```bash
curl -X POST "http://127.0.0.1:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=testuser&password=testpassword123"
```

### Access protected route
```bash
curl -X GET "http://127.0.0.1:8000/user/profile" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

---

## Security Considerations

- Passwords are hashed using **bcrypt** — never stored as plain text
- JWT tokens expire after 30 minutes
- Protected routes reject requests with missing or invalid tokens
- `.env` file is excluded from version control via `.gitignore`

---

## Project Structure
```
pale-api/
├── main.py              # App entry point
├── database.py          # Database connection and session
├── models.py            # SQLAlchemy User model
├── auth.py              # JWT and password hashing utilities
├── routes/
│   ├── users.py         # Register and login endpoints
│   └── protected.py     # Protected route
├── .env                 # Environment variables (not committed)
├── .env.example         # Safe template for environment variables
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

*Built by Phumla Mlotshwa — Palé Internship Application 2026*