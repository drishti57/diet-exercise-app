import streamlit as st
from diet_exercise_data import recommend_diet, recommend_exercise

# Set up page
st.set_page_config(page_title="Smart Diet & Exercise Recommender", layout="centered")
st.title("🍎 Smart Diet & Exercise Recommender")
st.markdown("Get personalized suggestions based on your health goals.")

# Collect User Input
age = st.number_input("Enter your age", min_value=5, max_value=100, value=20)
weight = st.number_input("Enter your weight (kg)", min_value=20, max_value=200, value=60)
goal = st.selectbox("Your Goal", ["Lose Weight", "Gain Weight", "Maintain Weight"])
activity_level = st.selectbox("Activity Level", ["Low", "Moderate", "High"])

# Button to trigger result
if st.button("Get My Plan"):
    diet = recommend_diet(age, weight, goal, activity_level)
    exercise = recommend_exercise(goal, activity_level)

    # Show results
    st.subheader("📝 Diet Plan:")
    for meal in diet:
        st.write("- " + meal)

    st.subheader("🏋️ Exercise Plan:")
    for ex in exercise:
        st.write("- " + ex)