from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Flask DevOps Pipeline v2</h1><p>Auto-deployed with GitHub Actions + Docker + AWS</p>"

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)