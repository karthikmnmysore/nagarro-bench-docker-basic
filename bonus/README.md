# Flask + Redis + PostgreSQL Application

This project is a **Flask-based web application** that integrates with **Redis** for visit counting and **PostgreSQL** for persistent user data storage.  
The setup is fully containerized using **Docker** and orchestrated via **Docker Compose**.

---

## 🚀 Features

- Flask API with endpoints for:
  - `GET /` → Welcome message
  - `GET /visits` → Count number of visits (stored in Redis)
  - `POST /users` → Add a new user (stored in PostgreSQL)
  - `GET /users` → List all users from PostgreSQL
- Redis for caching/visit counter
- PostgreSQL for persistent user data
- Docker + Docker Compose for easy setup

---

## 📦 Prerequisites

Ensure you have installed:

- [Docker](https://docs.docker.com/get-docker/)  
- [Docker Compose](https://docs.docker.com/compose/install/)  

---

## ⚙️ Setup & Run

1. **Clone the repository**  
   ```bash
   git clone <your-repo-url>
   cd <your-repo-name>

## Build and start the containers

**docker-compose up --build**

## Access the app

Flask API → http://localhost:5000

Redis → port 6379

PostgreSQL → port 5432

## Stop the containers

**docker-compose down**


## 📂 Project Structure

├── app.py

├── Dockerfile

├── docker-compose.yml

├── requirements.txt



## API Endpoints

```bash
# Home
GET /
Response:
Welcome to My Extended Flask App with Redis + Postgres!

# Visits Counter
GET /visits
Response Example:
Number of visits: 3

#  Add User
POST /users
Content-Type: application/json

{
  "name": "karthik"
}

Response Example:

{
  "message": "User karthik added!"
}

# List Users
GET /users

Response Example:

[
  { "id": 1, "name": "karthik" },
  { "id": 2, "name": "Ram" }
]

```

## 🛠️ Development Notes

- Flask runs in **debug mode** on port `5000`.  
- Redis runs on port `6379` (default).  
- PostgreSQL runs on **port 5432** with credentials defined in docker-compose.yml.
- Both Redis and PostgreSQL services are orchestrated alongside Flask using **Docker Compose**.



