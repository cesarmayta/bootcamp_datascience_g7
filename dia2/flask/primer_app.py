from flask import Flask

#creamos un objeto de clase Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<center><h1>Hola mundo con Flask</h1></center>'

app.run(debug=True)