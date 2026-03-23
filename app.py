from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL connection (DISABLED for deployment on Render)
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="A1HnZv16*",
#     database="portfolio"
# )
#
# cursor = db.cursor()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Database insert (DISABLED for deployment)
    # query = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
    # values = (name, email, message)
    # cursor.execute(query, values)
    # db.commit()

    # Instead of DB, just print (so app doesn't crash)
    print("New Form Submission:")
    print("Name:", name)
    print("Email:", email)
    print("Message:", message)

    return "Form Submitted Successfully!"


if __name__ == '__main__':
    app.run(debug=True)