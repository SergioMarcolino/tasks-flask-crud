from flask import Flask

# __name__ = "__main__" 
app = Flask(__name__)

@app.route("/")
def hello_word():
    return "Hello_World!"

@app.route("/about")
def sobre():
    return "Pagina sobre"

if __name__ == "__main__":
    app.run(debug=True, port=5001)