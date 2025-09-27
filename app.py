import streamlit as st
import pandas as pd
import random

# -----------------------------
# Load CSV data
# -----------------------------
diet_data = pd.read_csv("data/diet_tips.csv")
exercise_data = pd.read_csv("data/exercises.csv")

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Advanced Diet & Fitness Chatbot", page_icon="🍎")
st.title("Advanced Diet & Fitness Chatbot")
st.write("Type your question about diet or exercise, and I will give personalized suggestions!")

# -----------------------------
# User Input
# -----------------------------
user_input = st.text_input("Type your question here:")

# Optional: User personal info
age = st.number_input("Your Age:", min_value=5, max_value=120, value=25)
weight = st.number_input("Your Weight (kg):", min_value=10, max_value=200, value=60)
goal = st.selectbox("Your Goal:", ["Maintain Weight", "Lose Weight", "Gain Muscle", "Stay Fit"])

# -----------------------------
# Suggestion Logic
# -----------------------------
if st.button("Get Suggestion"):

    if user_input.strip() == "":
        st.warning("Please type your question first!")
    else:
        user_input_lower = user_input.lower()

        # Diet suggestions
        diet_matches = diet_data[diet_data['Keyword'].apply(lambda x: x.lower() in user_input_lower)]
        # Exercise suggestions
        exercise_matches = exercise_data[exercise_data['Keyword'].apply(lambda x: x.lower() in user_input_lower)]

        # Personalized tips based on goal
        personalized_note = ""
        if goal == "Lose Weight":
            personalized_note = "💡 Try to keep portions small and focus on high-protein, low-calorie foods."
        elif goal == "Gain Muscle":
            personalized_note = "💪 Include protein-rich meals and strength exercises."
        elif goal == "Maintain Weight":
            personalized_note = "⚖️ Balanced diet and regular exercise will help maintain your weight."
        elif goal == "Stay Fit":
            personalized_note = "🏃 Keep active daily and eat a variety of healthy foods."

        # Display suggestions
        if not diet_matches.empty:
            tip = random.choice(diet_matches['Tip'].tolist())
            st.success(f"💡 Diet Tip: {tip}\n{personalized_note}")
        elif not exercise_matches.empty:
            exercise = random.choice(exercise_matches['Exercise'].tolist())
            st.success(f"💪 Exercise Suggestion: {exercise}\n{personalized_note}")
        else:
            st.info("Sorry! I don't have a suggestion for that. Try keywords like breakfast, lunch, dinner, snack, cardio, strength, flexibility, abs, legs.")
