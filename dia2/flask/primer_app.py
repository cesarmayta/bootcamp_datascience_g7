from flask import Flask, request

#creamos un objeto de clase Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<center><h1>Hola mundo con Flask</h1></center>'

@app.route('/saludo')
def saludo():
    nombre = request.args.get('nombre','')
    return f"<h1>Hola {nombre}</h1>"

@app.route('/sumar/<int:a>/<int:b>')
def sumar(a,b):
    resultado = a + b
    return f"<center><h1>La suma de {a} + {b} es {resultado} </h1></center>"

app.run(debug=True)