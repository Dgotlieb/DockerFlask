import datetime
import os

from flask import Flask

app = Flask(__name__)

@app.route('/hello/<user_name>')
def user(user_name):
    now = str(datetime.datetime.now())
    users_file = open("logs/users.txt", mode='a')
    users_file.write(now + " " + user_name + "\n")
    return {now: user_name}


if __name__ == '__main__':
    os.makedirs("logs", exist_ok=True)
    app.run('0.0.0.0', debug=True, port=5000)
