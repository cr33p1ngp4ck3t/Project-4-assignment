import streamlit as st

st.title('BMI Calculator')

height = st.number_input('Enter your height in cm: ', min_value=100, max_value=250)
weight = st.number_input('Enter your weight in kg: ', min_value=40, max_value=200)

if height > 0 and weight > 0:
    bmi = weight / ((height / 100) ** 2)
    st.write('Your BMI is:', round(bmi, 2))

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"

    st.write(f'You fall into the **"{category}"** category.')
else:
    st.write("Please enter valid positive values for height and weight.")

st.markdown("""
### BMI Categories:
- **Underweight:** BMI < 18.5
- **Normal weight:** 18.5 <= BMI < 24.9
- **Overweight:** 25 <= BMI < 29.9
- **Obesity:** BMI >= 30
""")