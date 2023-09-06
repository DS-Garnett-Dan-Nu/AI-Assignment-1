import joblib
import streamlit as st
#type in " streamlit run assignment_3.py " in the terminal to run streamlit via localhost.

#Change the Radio Button input to Binary
def radio_to_num(des):

    input = st.radio(des, ("Yes", "No"))

    if input == "Yes":
        result = 1
        return result
    else:
        result = 0
        return result

# Load the pre-trained model
model = joblib.load("cost_cluster.joblib")

# Define the Streamlit app
st.title("Mobile Phone Cost Classifier")


# Input features
st.subheader("Battery Information")
battery = st.slider("Battery Capacity (mAh)", 500, 1999, 1500)
talk_time = st.slider("Battery Lifetime(Years)",2,20,3)

st.subheader("Processor Information")
n_core = st.slider("Number of Cores",1,8,4)
clock_speed = st.slider("CPU Speed",0.5,3.0,2.0)

st.subheader("Camera Information")
p_cam = st.slider("Primary Camera Megapixals",0,20,19)
fc = st.slider("Front Camera Megapixals", 0,19,12)

st.subheader("RAM and Storage")
storage = st.slider("RAM(MB)",263,3989,800)
memory = st.slider("Storage Capacity(GB)",2,64,8)

st.subheader("Mobile Phone Characteristics")
m_dep = st.slider("Thickness(inch)",0.1,1.0,0.2)
m_weig = st.slider("Weight(g)",80,200,100)
px_h = st.slider("Pixel Height",0,1907,47)
px_w = st.slider("Pixel Width",501,1998,559)
sc_h = st.slider("Screen Height(cm)",5,19,10)
sc_w = st.slider("Pixel Width(cm)",0,18,9)

st.subheader("Network Features")

#create 5 columns
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    dual_sim = radio_to_num("Dual Sim")
with col2:
    four_g = radio_to_num("4G")
with col3:
    three_g = radio_to_num("3G")
with col4:
    wifi = radio_to_num("Wifi")
with col5:
    blue = radio_to_num("Bluetooth")
with col6:
    touch_screen = radio_to_num("Touch Screen")

#Unchangable Values

# Make predictions
#if(st.button('Predict')):
features = [[battery, blue, clock_speed, dual_sim, fc, four_g, 
                    memory, m_dep, m_weig, n_core, p_cam, px_h, px_w, 
                    storage, sc_h, sc_w, talk_time, three_g, touch_screen, wifi]]
prediction = model.predict(features)






# Display prediction
st.sidebar.subheader("Predicted Mobile Cost Category:")
cost_categories = ["Low Cost", 
                   "Medium Cost", 
                   "High Cost"]

if prediction[0] == 0:
    st.sidebar.warning(cost_categories[prediction[0]])
elif prediction[0] == 1:
    st.sidebar.success(cost_categories[prediction[0]])
else:
    st.sidebar.error(cost_categories[prediction[0]])

# Probability scores.
prediction_probs = model.predict_proba(features)
st.sidebar.subheader("Prediction Probabilities:")
st.sidebar.write(
    {
    "Low Cost Probability":
    prediction_probs[0][0],
    "Medium Cost Probability": 
    prediction_probs[0][1],
    "High Cost Probability": 
    prediction_probs[0][2]
})
st.write("")
st.write("Assignment 3 by DS Garnett Dan Nu and Wai Yan Paing")


