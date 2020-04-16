import flask
from flask import jsonify, request
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/employees', methods=['GET', 'POST'])
def getAllEmployees():
    if request.method == 'POST':
        connect1 = sqlite3.connect('employee.db')
        cur = connect1.cursor()
        name = request.form['name']
        salary = request.form['salary']
        command ='INSERT INTO Employee (name,salary) VALUES (' + "\'"+name +"\'"+ ',' +"\'"+ salary + "\'"+')'
        print(command)
        cur.execute(command)
        connect1.commit()
        print(cur.rowcount)
        return ""
    elif request.method == 'GET':
        conn = sqlite3.connect('employee.db')
        cur = conn.cursor()
        all_emp = cur.execute('SELECT * FROM employee;').fetchall()
        return jsonify(all_emp)


@app.route('/employees/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def Employee(id):
    if request.method == 'GET':
        conn2 = sqlite3.connect('employee.db')
        cur = conn2.cursor()
        command ='SELECT * FROM Employee WHERE id ='+  "\'"+str(id)+"\'"
        emp= cur.execute(command).fetchone()
        return jsonify(emp)

    elif request.method == 'PUT':
        conn2 = sqlite3.connect('employee.db')
        cur = conn2.cursor()
        name = request.form['name']
        salary = request.form['salary']
        command = 'UPDATE Employee  SET name =' + "\'" + name + "\'" + ',' + "salary =" +\
                  "\'" + salary + "\'" + " WHERE id =" + "\'" + str(
            id) + "\'"
        cur.execute(command)
        conn2.commit()
        return ""
    elif request.method == 'DELETE':
        conn2 = sqlite3.connect('employee.db')
        cur = conn2.cursor()
        command = 'DELETE FROM employee WHERE id ='+ "\'"  + str(
            id) + "\'"
        cur.execute(command)
        conn2.commit()
        return ""

        return ""
app.run()
