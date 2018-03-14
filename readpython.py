from flask import Flask, json
from flask import render_template, request
import read
import sys

sys.path.insert(0, 'C:\Users\LONOVO\Desktop\MineriaDatos\Work1')

app = Flask(__name__)

@app.route('/') 
def index(): 
    return render_template('index.html')
@app.route('/design.css', methods=['GET'])
def design():
        return render_template('design.css')
#Recibimos los valores 
@app.route('/recibir',methods=['POST','GET'])
def recepcion():
    if request.method == 'POST':
        
            restText = open("rest.txt","w")
            Age = request.form['inputAge']
            Sex = request.form['inputSex']
            Bp = request.form['inputBp']
            Ch = request.form['inputCh']
            Nak = request.form['inputNak']
            restText.write(Age) 
            restText.write('\n')
            restText.write(Sex)
            restText.write('\n')
            restText.write(Bp)
            restText.write('\n')
            restText.write(Ch)
            restText.write('\n')
            restText.write(Nak)
            restText.write('\n')
            restText.close()       
            import NaiveBayes 
            
    else:
            print("No se ha posteado nada")
    return render_template('index.html')



app.run(debug = True, port = 8000) 