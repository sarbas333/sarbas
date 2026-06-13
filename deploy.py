import streamlit as st 
import pickle 
from PIL import Image

model=pickle.load(open('model.save','rb'))
scaler=pickle.load(open('scaler.save','rb'))
gend=pickle.load(open('gender.save','rb'))
sh=pickle.load(open('smoke.save','rb'))

def main():
    st.title('DIABETES PREDICTION')
    img=Image.open(r"C:\Users\User\Downloads\download (44).jpg")
    st.image(img)
    
    gender=st.selectbox('gender',['Female', 'Male'])
    age=st.text_input('AGE','type here')
    hyper=st.selectbox('HYPERTENSION',['yes','no'])
    if hyper=='yes':
        hyper=1
    else:
        hyper=0
        
    heart=st.selectbox('heart disease',['yes','no'])
    if heart=='yes':
        heart=1
    else:
        heart=0
        
    smoki=st.selectbox('SMOKING HISTORY',['never', 'No Info', 'current', 'former', 'ever', 'not current'])
    
    bmi=st.text_input('BMI','type here')
    hb=st.text_input('HbA1c_level','type here')
    bgl=st.text_input('blood_glucose_level','type here')
    
    
    pred=st.button('predict')
    
    gender1=gend.transform([gender])[0]
    smok=sh.transform([smoki])[0]
    
    f=[
        gender1,age,hyper,heart,smok,bmi,hb,bgl
    ]
    
    
    if pred:
        s=scaler.transform([f])
        m=model.predict(s)
        if m==0:
            st.success('sugar illa mone')
        else:
            st.error('sugar ind mone')
 
        


main()