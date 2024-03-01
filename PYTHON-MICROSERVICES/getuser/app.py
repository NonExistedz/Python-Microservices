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

#RESTAPIs
@app.route('/getuser/v1/<idmemo>', methods=["GET"])
def get_user(idmemo):
    cur = conn.reconnect()

    sql = "SELECT idmemo, firstname, lastname, email "
    sql += " FROM memo WHERE idmemo=%s ORDER BY firstname"
    data = (idmemo,)
    cur = conn.cursor()
    cur.execute(sql, data)
    records = cur.fetchone()
    conn.close()
    return jsonify(records)

@app.route('/getuser', methods=["GET"])
def get_user_all():
    cur = conn.reconnect()

    sql = "SELECT idmemo, firstname, lastname, email "
    sql += " FROM memo ORDER BY firstname"

    cur = conn.cursor()
    cur.execute(sql)
    records = cur.fetchall()
    conn.close()
    return jsonify(records)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)