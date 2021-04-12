from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Learning Heroku in praxis"

@app.route('/someendpoints')
def firstendpoint():
    return "first path"

if __name__ == "__main__":
    app.run()
