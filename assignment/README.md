# Simple Flask + Redis App

This project is a minimal **Flask web application** running inside **Docker Compose**, with **Redis** as a service.  

- Flask serves basic routes:
  - `/` → returns a welcome message
  - `/hello/<name>` → greets the user with their name
- Redis is included in `docker-compose.yml` (ready to extend for caching, sessions, etc.).

---

## 📂 Project Structure

├── app.py # Main Flask application
├── Dockerfile # Docker image build instructions
├── docker-compose.yml # Multi-container setup (Flask + Redis)
├── requirements.txt # Python dependencies



---

## ⚙️ Prerequisites

Make sure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)  
- [Docker Compose](https://docs.docker.com/compose/install/)  

---

## Setup & Run

```bash
# Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

# Build & start containers
docker-compose up --build

#  Stop containers
docker-compose down

Once running, open your browser at:
👉 http://localhost:5000


curl http://localhost:5000/
# Welcome to My Simple Flask App!

curl http://localhost:5000/hello/John
# Hello, John!


---

## 🛠️ Development Notes

- Flask runs in **debug mode** on port `5000`.  
- Redis runs on port `6379` (default).  
- Both services are orchestrated with Docker Compose.  
