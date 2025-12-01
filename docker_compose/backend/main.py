from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI Backend Running!"}

@app.get("/db-check")
def db_check():
    try:
        conn = psycopg2.connect(
            host="db",
            user="admin",
            password="admin123",
            dbname="devdb"
        )
        conn.close()
        return {"status": "Connected to PostgreSQL"}
    except Exception as e:
        return {"error": str(e)}
