from flask import Flask, render_template, request
from operacoes import *


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if(request.method== 'GET'):
        return render_template('index.html')
    else:
        if(request.form['opc']=='soma'):
            soma=int(request.form['num1'])+int(request.form['num2']) 
            return 'O valor da soma é ' +str(soma)
        if(request.form['opc']=='sub'):
            subtracao=int(request.form['num1'])-int(request.form['num2']) 
            return 'O valor da subtração é ' +str(subtracao)
        if(request.form['opc']=='div'):
            divisao=int(request.form['num1'])/int(request.form['num2']) 
            return 'O valor da divisão é ' +str(divisao)
        if(request.form['opc']=='mult'):
            multipicacao=int(request.form['num1'])*int(request.form['num2']) 
            return 'O valor da multiplicação é ' +str(multipicacao)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html')


app.run(port=4000, debug=True)
