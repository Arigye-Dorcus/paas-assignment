import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def init_database():
    try:
        conn = psycopg2.connect(os.environ.get("DATABASE_URL"))
        cur = conn.cursor()

        # Read and execute the schema file
        with open('schema.sql', 'r') as f:
            sql = f.read()
        
        cur.execute(sql)
        conn.commit()

        print("✅ Database initialized successfully!")
        print("Tables created: students, courses, enrollments")
        print("Sample data inserted.")

        cur.close()
        conn.close()

    except Exception as e:
        print(f"❌ Error initializing database: {e}")

if __name__ == '__main__':
    init_database()