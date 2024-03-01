from flask import Flask, request, redirect, jsonify
import mysql.connector as mysql

conn = mysql.connect(
    host="localhost",
    user = "root",
    password = "EDA3D2AD",
    port = 3306,
    database = "my_memo"
)

app = Flask(__name__)

@app.route('/put_user', methods=["PUT"])
def put_user():
    response = request.get_json()
    idmemo = response['idmemo']
    firstname = response['firstname']
    lastname = response['lastname']
    email = response['email']

#Update Data to Database
    cur = conn.reconnect()
    cur = conn.cursor()
    sql = "UPDATE memo SET firstname=%s, lastname=%s, email=%s "
    sql += " WHERE idmemo=%s "
    data = (firstname, lastname, email, idmemo)
    cur.execute(sql, data)
    conn.commit()
    conn.close()

    return redirect('http://localhost:5001/getuser')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)