from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

# Step 1: Get database URL from Render
DATABASE_URL = os.environ.get("DATABASE_URL")

# Step 2: Connect to PostgreSQL
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# Step 3: Create table automatically (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    message TEXT
);
""")
conn.commit()

# Step 4: Home page
@app.route('/')
def home():
    return render_template('index.html')

# Step 5: Form submission
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

# Step 6: SHOW DATA (VERY IMPORTANT 🔥)
@app.route('/data')
def show_data():
    cursor.execute("SELECT * FROM contacts")
    data = cursor.fetchall()
    return str(data)

# Step 7: Run app
if __name__ == '__main__':
    app.run(debug=True)