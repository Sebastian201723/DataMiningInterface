from flask import Flask, json
from flask import render_template, request
import sys

sys.path.insert(0, 'C:\Users\LONOVO\Desktop\MineriaDatos\Work1')

import read
import NaiveBayes 

#Probabilidades importadas desde work1
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
    
def show():
    return (json.dumps({'TOTALProbTotal1N: ',NaiveBayes.TOTALProbTotal1N}))

@app.route('/design.css', methods=['GET', 'POST'])
def design():
        return render_template('design.css')
#Recibimos los valores 
@app.route('/recibir',methods=['POST','GET'])
def recepcion():
    if request.method == 'POST':
            Age = request.form['inputAge']
            AgeText = open("AgeText.txt","w")
            AgeText.write(Age) 
            AgeText.close()
            Sex = request.form['inputSex']
            SexText = open("SexText.txt","w")
            SexText.write(Sex) 
            SexText.close()
            Bp = request.form['inputBp']
            BpText = open("BpText.txt","w")
            BpText.write(Bp) 
            BpText.close()
            Ch = request.form['inputCh']
            ChText = open("ChText.txt","w")
            ChText.write(Ch) 
            ChText.close()
            Nak = request.form['inputNak']
            NakText = open("NakText.txt","w")
            NakText.write(Nak) 
            NakText.close()
    else:
            print("No se ha posteado nada")
    return render_template('index.html')
app.run(debug = True, port = 8000) 