import streamlit as st
import joblib
model_nb=joblib.load('spam-ham')
st.title('SPAM-HAM CLASSIFIER') #creates a title with name spam-ham classifier
ip=st.text_input('Enter the Message:') #creates a text box
op=model_nb.predict([ip])
if st.button('Predict'):
  st.title(op[0]) #prints the output as spam or ham
