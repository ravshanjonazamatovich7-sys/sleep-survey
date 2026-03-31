import streamlit as st

st.title("Social Media & Sleep Quality Survey")

name = st.text_input("Enter your name")
dob = st.text_input("Enter DOB (DD/MM/YYYY)")
student_id = st.text_input("Enter Student ID")

questions = [
    "I use my phone within 30 minutes before sleeping.",
    "I spend more time on social media at night than planned.",
    "Social media delays my bedtime.",
    "Notifications wake me during the night.",
    "I check my phone immediately after waking up.",
    "I feel tired in the morning.",
    "I struggle to fall asleep after phone use.",
    "I lose track of time scrolling.",
    "I feel sleepy during classes.",
    "I have difficulty concentrating.",
    "I feel anxious without checking my phone.",
    "I wake up to check social media.",
    "My sleep schedule changes due to phone use.",
    "I feel physically exhausted.",
    "My sleep quality is affected by social media."
]

options = {
    "Never": 0,
    "Rarely": 1,
    "Sometimes": 2,
    "Often": 3,
    "Always": 4
}

responses = []

for q in questions:
    answer = st.radio(q, list(options.keys()))
    responses.append(options[answer])

def get_result(score):
    if score <= 20:
        return "Excellent Sleep Quality"
    elif score <= 40:
        return "Good Sleep Quality"
    elif score <= 60:
        return "Moderate Sleep Issues"
    elif score <= 75:
        return "Poor Sleep Quality"
    else:
        return "Severe Sleep Problems"

if st.button("Submit"):
    total = sum(responses)
    result = get_result(total)

    st.subheader("Result")
    st.write("Score:", total)
    st.write("Condition:", result)
