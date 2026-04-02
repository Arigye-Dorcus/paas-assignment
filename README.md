# PaaS Assignment – Flask App on Railway

A simple web application demonstrating Platform-as-a-Service deployment 
using Railway, Python Flask, and PostgreSQL.

## Live URL
https://your-app-name.up.railway.app

## GitHub Repository
https://github.com/YOUR_USERNAME/paas-assignment

---

## Tech Stack
- **Language:** Python 3.11
- **Framework:** Flask
- **Database:** PostgreSQL (Railway managed)
- **Hosting:** Railway (PaaS)
- **CI/CD:** GitHub + Railway auto-deploy

---

## Features
- Full CRUD operations on Students and Courses
- PostgreSQL database integration
- Environment variable configuration
- Auto-deployment via GitHub push

---

## API Endpoints

### Students
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/students` | Get all students |
| POST | `/students` | Add a new student |
| PUT | `/students/<id>` | Update a student |
| DELETE | `/students/<id>` | Delete a student |

### Courses
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/courses` | Get all courses |
| POST | `/courses` | Add a new course |
| PUT | `/courses/<id>` | Update a course |
| DELETE | `/courses/<id>` | Delete a course |

### Enrollments
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/enrollments` | Get all enrollments |
| POST | `/enrollments` | Enroll a student in a course |

---

## Environment Variables

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | PostgreSQL connection string (set by Railway) |
| `SECRET_KEY` | App secret key |
| `FLASK_ENV` | Environment (development/production) |
| `PORT` | Port number (set by Railway) |

---

## Local Setup
```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/paas-assignment.git
cd paas-assignment

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up local environment variables
cp .env.example .env  # Then edit .env with your values

# Initialize the database
python init_db.py

# Run the app
python app.py
```

---

## Deployment (Railway)

1. Push code to GitHub
2. Connect repo to Railway
3. Add PostgreSQL database service
4. Environment variables are auto-configured
5. Every push to `main` triggers auto-redeployment

---

## Database Schema

**students** — stores student records  
**courses** — stores course information  
**enrollments** — links students to courses (many-to-many)
```

---

## `.env.example`
*(a safe template others can copy — has no real values)*
```
DATABASE_URL=postgresql://username:password@localhost/dbname
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
PORT=5000