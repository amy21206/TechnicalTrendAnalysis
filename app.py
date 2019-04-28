from flask import Flask

app = Flask(__name__)
app.config['debug'] = True

@app.route("/")
def hello():
  return "Hello World!"