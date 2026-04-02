from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db():
    return psycopg2.connect(os.environ.get("DATABASE_URL"))

@app.route('/')
def home():
    return "PaaS Assignment App is running!"

# CREATE
@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, email) VALUES (%s, %s) RETURNING id",
                (data['name'], data['email']))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close(); conn.close()
    return jsonify({"id": new_id, "message": "Student added"}), 201

# READ
@app.route('/students', methods=['GET'])
def get_students():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM students")
    rows = cur.fetchall()
    cur.close(); conn.close()
    return jsonify([{"id": r[0], "name": r[1], "email": r[2]} for r in rows])

# UPDATE
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE students SET name=%s, email=%s WHERE id=%s",
                (data['name'], data['email'], id))
    conn.commit()
    cur.close(); conn.close()
    return jsonify({"message": "Student updated"})

# DELETE
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    cur.close(); conn.close()
    return jsonify({"message": "Student deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))


