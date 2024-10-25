from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Flask on dcrypto.site!"

if __name__ == "__main__":
    app.run(host="http://145.223.19.67/", port=5000)
