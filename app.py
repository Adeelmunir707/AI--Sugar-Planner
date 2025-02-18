import streamlit as st
import google.generativeai as genai

# Load Google API Key
api_key = st.secrets["google_api_key"]
genai.configure(api_key=api_key)

# Function to call Google Gemini API and get a personalized meal plan
def get_meal_plan(fasting_sugar, pre_meal_sugar, post_meal_sugar, dietary_preferences):
    model = genai.GenerativeModel("gemini-1.5-pro")

    prompt = (
        f"My fasting sugar level is {fasting_sugar} mg/dL, "
        f"my pre-meal sugar level is {pre_meal_sugar} mg/dL, "
        f"and my post-meal sugar level is {post_meal_sugar} mg/dL. "
        f"My dietary preferences are {dietary_preferences}. "
        "You are a world-class nutritionist who specializes in diabetes management. Please provide a personalized meal plan that can help me manage my blood sugar levels effectively."
    )

    response = model.generate_content(prompt)
    return response.text

# Streamlit app
st.set_page_config(page_title="Diet Balance", page_icon="🥗", layout="centered")
st.title("Bite Balance")

st.write("""
**Diet Balance** an AI personalized meal planning tool designed specifically for diabetic patients. 
By entering your sugar levels and dietary preferences, Diet Balance generates meal plans that are 
tailored to help you manage your blood sugar levels effectively.
""")

# Sidebar inputs for sugar levels and dietary preferences
st.sidebar.header("Enter Your Details")

fasting_sugar = st.sidebar.number_input("Fasting Sugar Levels (mg/dL)", min_value=0, max_value=500, step=1)
pre_meal_sugar = st.sidebar.number_input("Pre-Meal Sugar Levels (mg/dL)", min_value=0, max_value=500, step=1)
post_meal_sugar = st.sidebar.number_input("Post-Meal Sugar Levels (mg/dL)", min_value=0, max_value=500, step=1)

dietary_preferences = st.sidebar.text_input("Dietary Preferences (e.g., vegetarian, low-carb)")

# Generate meal plan button
if st.sidebar.button("Generate Meal Plan"):
    meal_plan = get_meal_plan(fasting_sugar, pre_meal_sugar, post_meal_sugar, dietary_preferences)
    st.write("Based on your sugar levels and dietary preferences, here is a personalized meal plan:")
    st.markdown(meal_plan)

st.write("\n" * 15)
# Add a bold line above the footer
st.markdown("<hr style='border: 2px solid black;'>", unsafe_allow_html=True)
# Footer content
st.write("Copy© 2025 Adeel Munir | Made With ❤️ in Pakistan")
