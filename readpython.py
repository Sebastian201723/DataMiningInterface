from flask import Flask, json
from flask import render_template, request
import sys

sys.path.insert(0, 'c:\\Users\LONOVO\Desktop\MineriaDatos\Work1')

import read
import NaiveBayes 

NaiveBayes.TOTALProbTotal1N
NaiveBayes.TOTALProbTotal2N
NaiveBayes.TOTALProbTotal3N
NaiveBayes.TOTALProbTotal4N
NaiveBayes.TOTALProbTotal5N

NaiveBayes.classResul

print("Constante Prob total 1: ", NaiveBayes.TOTALProbTotal1N)
print("Constante class resultante: ", NaiveBayes.classResul)

app = Flask(__name__)

@app.route('/') 
def index(): 
    return render_template('index.html')
#url_for('static', filename='/stylesheet/design.css')
    
def show():
    return (json.dumps({'TOTALProbTotal1N: ',NaiveBayes.TOTALProbTotal1N}))

@app.route('/design.css', methods=['GET'])
def design():
        return render_template('design.css')
#Recibimos los valores 
@app.route('/recibir',methods=['POST','GET'])
def recepcion():
    print("Entramos!!!")
    if request.method == 'POST':
            Age = request.form['inputAge']
            Sex = request.form['inputSex']
            Bp = request.form['inputBp']
            print("Bp:",Bp)
            Ch = request.form['inputCh']
            print("Ch:",Ch)
            Nak = request.form['inputNak']
            print("salimos: Nak: ", Nak)
    else:
            print("No ha entrado SENORES!")
    return render_template('index.html')
app.run(debug = True, port = 8000)