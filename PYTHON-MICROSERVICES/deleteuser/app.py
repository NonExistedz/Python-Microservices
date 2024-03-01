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

@app.route('/delete/<email>', methods=["DELETE"])
def delete_user(email):
    cur = conn.reconnect()
    cur = conn.cursor()
    sql = "DELETE FROM memo WHERE email =%s"
    data = (email,)
    cur.execute(sql,data)
    conn.commit()
    conn.close()
    return redirect('http://localhost:5001/getuser')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)