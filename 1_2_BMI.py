import streamlit as st 

# da title
st.title('Welcome to BMI Calculater')
st.text("DS's Version")

# take weight and height
weight = st.number_input("Enter your weight (in kgs)")
height = st.number_input("Enter your height (in cms)")

#try???
try:
    bmi = weight / ((height/100)**2)
except:
    st.text("Enter some value of height")

# check button pressed
if(st.button('Calculate BMI')):

    #print BMI index 
    st.text("Your BMI Index id {}.".format(bmi))

    # BMI ifo
    if(bmi <16):
        st.error("You need to Eat a Horse, Everyday.")
    elif(bmi >= 16 and bmi <18.5):
        st.warning("You should Eat a Burger or Two.")
    elif(bmi>= 18.5 and bmi < 25):
        st.success("*Giga Chad Music plays")
    elif(bmi >= 25 and bmi < 30):
        st.warning("You should Umm... Slow Down on Carbs?")
    elif(bmi >= 30):
        st.error("Stop Eating, Start Exercising")

# deployed app link = https://ds-bmi.streamlit.app/