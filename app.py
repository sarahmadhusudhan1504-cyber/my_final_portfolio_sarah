from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# ✅ Your Render Database URL
DATABASE_URL = "postgresql://portfolio_db_gb3f_user:g9zWEMMCB7PadKSN5BlRqKtLmwOt6iOU@dpg-d6tqpb24d50c73cft1bg-a.oregon-postgres.render.com/portfolio_db_gb3f"


# ✅ Function to create connection (BEST PRACTICE)
def get_connection():
    return psycopg2.connect(DATABASE_URL)


# ✅ Create table (runs once at start)
conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    message TEXT
);
""")
conn.commit()
cursor.close()
conn.close()


# ✅ Home page
@app.route('/')
def home():
    return render_template('index.html')


# ✅ Form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)",
        (name, email, message)
    )
    conn.commit()

    cursor.close()
    conn.close()

    return "FORM SUBMITTED SUCCESSFULLY !! [Stored in database!]"


# ✅ Show data
@app.route('/data')
def show_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM contacts")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return str(data)


# ✅ Run app
if __name__ == '__main__':
    app.run(debug=True)