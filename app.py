from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "Keep going!",
    "You're doing great!",
    "Every day is a new beginning!",
    "Believe in yourself!",
    "Success is built on consistency."
]

@app.route('/')
def home():
    return f"<h1>{random.choice(quotes)}</h1>"

if __name__ == "__main__":
    app.run()