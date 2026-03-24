from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

#Get database URL from Render
DATABASE_URL = os.environ.get("DATABASE_URL")

#Connect to PostgreSQL
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# Create table automatically (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    message TEXT
);
""")
conn.commit()

#Home page
@app.route('/')
def home():
    return render_template('index.html')

#Form submission
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

    return "FORM SUBMITTED SUCESSFULLY !! [Stored in database!]"

# TO show DATA 
@app.route('/data')
def show_data():
    cursor.execute("SELECT * FROM contacts")
    data = cursor.fetchall()
    return str(data)

#Run app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
