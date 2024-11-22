from flask import Flask, request, render_template, redirect, url_for, session
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)