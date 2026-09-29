from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>CI/CD Cloud Demo</title>
        </head>
        <body>
            <h1>CI/CD Pipeline Successful!</h1>
            <p>Application deployed using GitHub and Cloud Platform.</p>
            <p>Build → Test → Deploy</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)