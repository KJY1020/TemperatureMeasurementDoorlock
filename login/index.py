from flask import Flask, render_template, request
from db import Database

logindb = Database.Database()
app = Flask(__name__)

@app.route("/")
def login():
    return render_template('index.html')

@app.route("/post", methods=['POST'])
def post():
    userID = request.form['inputID']
    userPW = request.form['inputPW']
    msg = logindb.insertLogin(userID, userPW)
    #msg += "ip : %s"%request.remote_addr   => 사용자ip확인
    return msg

if __name__ == "__main__":
    app.run(host="0.0.0.0")
