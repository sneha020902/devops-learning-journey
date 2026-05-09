from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Flask DevOps Pipeline v2</h1><p>Auto-deployed with GitHub Actions + Docker + AWS</p>"

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/status")
def status():
    return jsonify({
        "status": "running",
        "app": "Flask DevOps Pipeline",
        "version": "2.0",
        "timestamp": datetime.datetime.utcnow().isoformat()
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)