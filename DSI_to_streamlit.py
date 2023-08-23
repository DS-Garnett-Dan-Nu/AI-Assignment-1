import streamlit as st 
import joblib

# da title
st.title('Welcome to DSI Fish Weight Calculater')
st.text("Assignment 1 by DS and Hsi")

# take parameters
l1 = st.number_input("Enter your Length 1 (in cm)")
l2 = st.number_input("Enter your Length 2 (in cm)")
l3 = st.number_input("Enter your Length 3 (in cm)")
h = st.number_input("Enter your Height (in cm)")
w = st.number_input("Enter your Width (in cm)")


X_test = [[l1,l2,l3,h,w]]
#X_test = [[12,14,16,5,15]]

model = joblib.load("DSI_fish_model.joblib")

result = model.predict(X_test)


# check button pressed
if(st.button('Calculate Fish Weight')):

    if l1 > 0 and l2 > 0 and l3 > 0 and h > 0 and w > 0:

        #fish weight yay!
        st.success("Length 1 = ",l1," cm.")
        st.success("Length 2 = {} cm.".format(l2))
        st.success("Length 3 = {} cm.".format(l3))
        st.success("Height = {} cm.".format(h))
        st.success("Width = {} cm.".format(w))
        st.success("Your Fish Weight is {} g.".format(result[0][0]))

    else:

        st.error("One of your values is INVALID. Please Try Again.")

