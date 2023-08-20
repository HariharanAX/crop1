from flask import Flask,request
import numpy as np

import pickle

# importing model
model = pickle.load(open(r"C:\Users\hariharan\Desktop\Modified Data\trained model.pkl",'rb'))


# creating flask app
app = Flask(__name__)



@app.route('/predict/<a>/<b>/<c>/<d>/<e>/<f>/<g>')
def predict(a,b,c,d,e,f,g):
    a1=float(a)
    b1=float(b)
    c1=float(c)
    d1=float(d)
    e1=float(e)
    f1=float(f)
    g1=float(g)
    return {
        "ANSWER " : str(model.predict(np.array([[a1,b1,c1,d1,e1,f1,g1]])))
    }


if __name__ == "__main__":
    app.run(debug=True)