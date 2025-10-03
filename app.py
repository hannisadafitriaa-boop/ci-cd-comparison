from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, CI/CD with GitHub Actions & Jenkins!"

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    # Gunakan port dari environment variable (Heroku pakai ini)
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
