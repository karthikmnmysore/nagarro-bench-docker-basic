from flask import Flask, request, jsonify
import redis, os
from sqlalchemy import create_engine, text

app = Flask(__name__)

# Redis config
redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

# Database config
db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url, echo=True, future=True)

@app.route("/")
def home():
    return "Welcome to My Extended Flask App with Redis + Postgres!"

@app.route("/visits")
def visits():
    count = r.incr("counter")
    return f"Number of visits: {count}"

@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    with engine.begin() as conn:
        conn.execute(text("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT)"))
        conn.execute(text("INSERT INTO users (name) VALUES (:name)"), {"name": name})
    return jsonify({"message": f"User {name} added!"})

@app.route("/users", methods=["GET"])
def list_users():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT id, name FROM users"))
        users = [{"id": row.id, "name": row.name} for row in result]
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

