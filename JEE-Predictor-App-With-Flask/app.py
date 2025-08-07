from flask import Flask
import mysql.connector
from flask import request, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/predict", methods=["POST"])
def predict():
    marks=request.form['marks']
    date=request.form['date']
    phone=request.form['phone']
    email=request.form['email']
    shift=request.form['shift']
    print(date, shift, marks, phone, email)
    conn=mysql.connector.connect(
        host="localhost",
        password="Varun@06",
        user="root",
        database="JEE_PREDICTOR"
    )
    cursor=conn.cursor()
    
    query = "INSERT INTO students (marks, exam_date, shift, phone, email) VALUES (%s, %s, %s, %s, %s)"
    values = (marks, date, shift, phone, email)
    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()
    return render_template('result.html', marks=marks,date=date,phone=phone,email=email,shift=shift,percentile=98.0)


if __name__ == "__main__":
    app.run(debug=True)