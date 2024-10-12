from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data['name']
    roll_number = data['roll_number']
    course = data['course']
    email = data['email']
    
    conn = create_connection('../database/students.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students (name, roll_number, course, email)
        VALUES (?, ?, ?, ?)
    ''', (name, roll_number, course, email))
    conn.commit()
    conn.close()

    return jsonify({"message": "Student added successfully!"}), 201

@app.route('/students', methods=['GET'])
def get_students():
    conn = create_connection('../database/students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True)
