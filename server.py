from flask import Flask
import socket
import subprocess

app = Flask(__name__)

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

@app.route('/', methods=['POST'])
def compute():
    subprocess.Popen(["python3", "stress_cpu.py"])
    return "Started CPU stress process", 202


@app.route("/", methods=['GET'])
def get_me():
    return ip_address, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    # app.run(host='0.0.0.0', port=5000, debug=True)