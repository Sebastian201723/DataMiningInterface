from flask import Flask, json
from flask import render_template
import sys

sys.path.insert(0, 'c:\\Users\LONOVO\Desktop\MineriaDatos\Work1')

import read
import NaiveBayes 
NaiveBayes.TOTALProbTotal1N
print("Constante: ", NaiveBayes.TOTALProbTotal1N)
app = Flask(__name__)

@app.route('/')
 
def index(): 
    return render_template('index.html')
def show():
    return (json.dumps({'TOTALProbTotal1N':NaiveBayes.TOTALProbTotal1N}))
app.run(debug = True, port = 8000)