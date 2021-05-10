from flask import Flask
app = Flask(__name__)
@app.route('/')
def hi_there():
    x = 3
    y = 4
    print(x)
    