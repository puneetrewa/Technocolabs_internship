import pickle
import numpy as np
import pandas as pd
import streamlit as st




mod = pickle.load(open('model.pkl','rb'))

def predict_disease(df):
    pred1 = mod.predict(df)
    print(pred1)
    return pred1



def main():
    st.title("Parkinsons Disease")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    a = st.text_input("",key=1)
    b = st.text_input("",key=2)
    c = st.text_input("",key=3)
    d = st.text_input("",key=4)
    e = st.text_input("",key=5)
    f = st.text_input("",key=6)
    g = st.text_input("",key=7)
    h = st.text_input("",key=8)
    i = st.text_input("",key=9)
    j = st.text_input("	",key=10)
    k = st.text_input("",key=11)
    l = st.text_input("",key=12)
    m = st.text_input("",key=13)
    n = st.text_input("",key=14)
    o = st.text_input("",key=15)
    p = st.text_input("",key=16)
    q = st.text_input("",key=17)
    r = st.text_input("",key=18)
    s = st.text_input("",key=19)
    t = st.text_input("",key=20)
    u = st.text_input("",key=21)
    v = st.text_input("",key=22)

    
    arr = [[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v]]
    lst = arr 
    df = pd.DataFrame(lst, columns=['MDVP:Fo(Hz)','MDVP:Fhi(Hz)','MDVP:Flo(Hz)','MDVP:Jitter(%)','MDVP:Jitter(Abs)','MDVP:RAP','MDVP:PPQ','Jitter:DDP','MDVP:Shimmer','MDVP:Shimmer(dB)','Shimmer:APQ3', 'Shimmer:APQ5','MDVP:APQ','Shimmer:DDA','NHR','HNR','RPDE','DFA','spread1','spread2','D2','PPE']) 
    result = ""

    if st.button("Predict"):
        result = predict_disease(df)
    st.success('Output disease {}'.format(result))
    if st.button("About"):
        st.text("Puneet Tiwari")  

if __name__=='__main__':
    main()