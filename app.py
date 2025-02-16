import streamlit as st
import anthropic

api_key = st.secrets["claude_api_key"]

def get_meal_plan(api_key, fasting_sugar, pre_meal_sugar, post_meal_sugar, dietary_preferences):
    try:
        client = anthropic.Anthropic(api_key=api_key)

        prompt = (
            f"My fasting sugar level is {fasting_sugar} mg/dL, "
            f"my pre-meal sugar level is {pre_meal_sugar} mg/dL, "
            f"and my post-meal sugar level is {post_meal_sugar} mg/dL. "
            f"My dietary preferences are {dietary_preferences}. "
            "Please provide a personalized meal plan that can help me manage my blood sugar levels effectively."
        )

        response = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=250,
            temperature=0.7,
            system="You are a world-class nutritionist who specializes in diabetes management.",
            messages=[{"role": "user", "content": prompt}]
        )

        # Print response to debug format
        st.write("Claude API Response:", response.content)

        # Extract and return text
        if isinstance(response.content, list) and len(response.content) > 0:
            return response.content[0]["text"]
        else:
            return "Sorry, an error occurred in generating the meal plan."

    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("GlucoGuide")
st.sidebar.header("Enter Your Details")

fasting_sugar = st.sidebar.number_input("Fasting Sugar Levels (mg/dL)", min_value=0, max_value=500, step=1)
pre_meal_sugar = st.sidebar.number_input("Pre-Meal Sugar Levels (mg/dL)", min_value=0, max_value=500, step=1)
post_meal_sugar = st.sidebar.number_input("Post-Meal Sugar Levels (mg/dL)", min_value=0, max_value=500, step=1)
dietary_preferences = st.sidebar.text_input("Dietary Preferences (e.g., vegetarian, low-carb)")

if st.sidebar.button("Generate Meal Plan"):
    meal_plan = get_meal_plan(api_key, fasting_sugar, pre_meal_sugar, post_meal_sugar, dietary_preferences)
    st.write("Here is your personalized meal plan:")
    st.markdown(meal_plan)
