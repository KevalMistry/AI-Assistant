from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Your AI Assistant is running on Railway 🚀"

if __name__ == "__main__":
    app.run(debug=True)