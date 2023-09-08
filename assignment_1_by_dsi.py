import streamlit as st 
import joblib

# reassign da species
def species(input):
    x = {
        'Bream':0,
        'Roach':1,
        'White Fish':2,
        'Parkki':3,
        'Perch':4,
        'Pike':5,
        'Smelt':6
         }
    return x[input]


# da title
st.title('DSI Fish Weight Prediction')
st.text("Assignment 1 by DS Garnett Dan Nu and Wai Yan Paing")

# take parameters
sp = st.selectbox("Species",["Bream","Roach","White Fish","Parkki","Perch","Pike","Smelt"])
l1 = st.number_input("Enter your Length 1 (in cm)")
l2 = st.number_input("Enter your Length 2 (in cm)")
l3 = st.number_input("Enter your Length 3 (in cm)")
h = st.number_input("Enter your Height (in cm)")
w = st.number_input("Enter your Width (in cm)")

spn = species(sp)

X_test = [[spn,l1,l2,l3,h,w]]
#X_test = [[12,14,16,5,15]]

model = joblib.load("fish_model.joblib")

result = model.predict(X_test)
result_real = str("%.1f" % result[0][0])

# check button pressed
if(st.button('Predict Fish Weight')):

    if l1 > 0 and l2 > 0 and l3 > 0 and h > 0 and w > 0:

        #fish weight yay!
        st.write('''
        Attributes of the Fish   
        Specie = {}.  
        Length 1 = {} cm.  
        Length 2 = {} cm.  
        Length 3 = {} cm.  
        Height = {} cm.  
        Width = {} cm.  
        '''.format(sp,l1,l2,l3,h,w))

        if result[0][0] <= 0:
            st.error(f"Fish Weight is {result_real} g. Fish Weight is INVAILID.")
        elif result[0][0] <= 1000:
            st.warning(f"Fish Weight is {result_real} g. Fish is Illegal.")
        elif result[0][0] <= 10000:
            st.success(f"Fish Weight is {result_real} g. Fish is Legal.")
        elif result[0][0] > 10000:
            st.warning(f"Fish Weight is {result_real} g. Fish is Illegal.")

    else:

        st.error("One of your values is INVALID. Please Try Again.")
