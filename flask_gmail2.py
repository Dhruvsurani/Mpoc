from flask import Flask

app = Flask("google auth")

@app.route("/login")
def login():
    pass


@app.route("/callback")
def callback():
    pass

@app.route("/")
def index():
    return 'hello'


if __name__ == "__main__":
    app.run(debug=True)
