

from TablaSimbolos.Arbol import Arbol
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from grammar import parse
app = Flask(__name__)
CORS(app,resources={r'/*':{"origins":"*"}})



auxGlobal=['','','']


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/Bienvenida")
def welcome():
    return render_template('index.html')

@app.route("/Analisis", methods=["POST","GET"])
def analyze():
    global auxGlobal
    if request.method == "POST":
        inpt = request.json["input"];        
        auxGlobal = parse(inpt)
        if isinstance(auxGlobal[0],Arbol):
            console = auxGlobal[0].getConsola()
            grafo = auxGlobal[1]
            simbolos = auxGlobal[2]

            arreglo=[console,grafo,simbolos]
            print(arreglo)
        return jsonify(console)
    else:
        
        return render_template('index.html')

@app.route('/Reportes')
def REPORTS():                
        return render_template('index.html')

@app.route('/AST', methods=["POST","GET"])
def AST():            
    if request.method == "POST":    
        return jsonify(auxGlobal[1])
    else:        
        return render_template('index.html')

@app.route('/TablaSimbolos', methods=["POST","GET"])
def Symbols():            
    if request.method == "POST":    
        return jsonify(auxGlobal[2])
    else:        
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False)