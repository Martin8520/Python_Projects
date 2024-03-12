from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, world!"


@app.route("/fancy")
def hello_world_fancy():
    return """
    <html>
    <body>
    
    <h1>Greetings!</h1>
    <p>Hello, world!</p>
    
    </body>
    </html>
    """