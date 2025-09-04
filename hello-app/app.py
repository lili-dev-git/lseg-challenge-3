from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def index():
    secret_msg = os.getenv("HELLO_SECRET_MSG", "no-secret")
    return f"Hello, SRE! Secret says: {secret_msg}\n"

@app.get("/healthz")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
