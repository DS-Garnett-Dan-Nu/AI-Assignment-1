import streamlit as st 
import joblib

# da title
st.title('Welcome to DSI Fish Weight Calculater')
st.text("Assignment 1 by DS and Hsi")

# take parameters
l1 = st.number_input("Enter Fish Length 1 (in cm)")
l2 = st.number_input("Enter Fish Length 2 (in cm)")
l3 = st.number_input("Enter Fish Length 3 (in cm)")
h = st.number_input("Enter Fish Height (in cm)")
w = st.number_input("Enter Fish Width (in cm)")


X_test = [[l1,l2,l3,h,w]]
#X_test = [[12,14,16,5,15]]

model = joblib.load("DSI_fish_model.joblib")

result = model.predict(X_test)

# check button pressed
if(st.button('Predict Fish Weight')):

    if l1 > 0 and l2 > 0 and l3 > 0 and h > 0 and w > 0:

        #fish weight yay!
        st.success('''
        Attributes of the Fish  
        Length 1 = {} cm.  
        Length 2 = {} cm.  
        Length 3 = {} cm.  
        Height = {} cm.  
        Width = {} cm.  
        '''.format(l1,l2,l3,h,w))

        if result[0][0] <= 0:
            st.error("Fish Weight is {} g. Fish Weight is INVAILID.".format(result[0][0]))
        elif result[0][0] <= 500:
            st.success("Fish Weight is {} g. Fish is Illegal.".format(result[0][0]))
        elif result[0][0] <= 2500:
            st.success("Fish Weight is {} g. Fish is Legal.".format(result[0][0]))
        elif result[0][0] > 2500:
            st.warning("Fish Weight is {} g. Fish is Illegal.".format(result[0][0]))

    else:

        st.error("One of your values is INVALID. Please Try Again.")

