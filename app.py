from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

# Get DB URL from Render
DATABASE_URL = os.environ.get("DATABASE_URL")

# Connect to PostgreSQL
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# Create table automatically
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    message TEXT
);
""")
conn.commit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    cursor.execute(
        "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)",
        (name, email, message)
    )
    conn.commit()

    return "Stored in database!"

if __name__ == '__main__':
    app.run(debug=True)