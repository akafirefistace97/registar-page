from flask import Flask, render_template, request
#importing database module
import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='webg_python')
cursor = cnx.cursor()

app=Flask(__name__)

@app.route('/view')
def view():
	query = "SELECT users.*, colleges.college_name FROM users INNER JOIN colleges ON users.college_id = colleges.id"
	cursor.execute(query)
	result = cursor.fetchall()
	cnx.commit()
	return render_template('view.html', data=result)

@app.route('/getdata'):
def getdata():
	return "getdata"


app.run(debug=True)