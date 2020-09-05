from flask import Flask,jsonify,render_template,request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

mod = pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])

def predict(): 
    features = [[x for x in request.form.values()]]
    df = pd.DataFrame(features,columns = ['MDVP:Fo(Hz)','MDVP:Fhi(Hz)','MDVP:Flo(Hz)','MDVP:Jitter(%)','MDVP:Jitter(Abs)','MDVP:RAP','MDVP:PPQ','Jitter:DDP','MDVP:Shimmer','MDVP:Shimmer(dB)','Shimmer:APQ3', 'Shimmer:APQ5','MDVP:APQ','Shimmer:DDA','NHR','HNR','RPDE','DFA','spread1','spread2','D2','PPE'])
    prediction = mod.predict(df)
    output = prediction
    if output>str(0.5):
        return render_template('index.html',pred = 'Parkinsons disease detected')
    else:
        return render_template('index.html',pred = 'Parkinsons not detected')


if __name__ == "__main__":
    app.run(debug= True)              


