import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Load model and tokenizer once (outside function to avoid reloading)
MODEL_NAME = "deepseek-ai/DeepSeek-R1"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, trust_remote_code=True)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def get_meal_plan(fasting_sugar, pre_meal_sugar, post_meal_sugar, dietary_preferences):
    """Generates a meal plan based on the user's sugar levels and dietary preferences."""
    
    prompt = (
        f"My fasting sugar level is {fasting_sugar} mg/dL, "
        f"my pre-meal sugar level is {pre_meal_sugar} mg/dL, "
        f"and my post-meal sugar level is {post_meal_sugar} mg/dL. "
        f"My dietary preferences are {dietary_preferences}. "
        "You are a world-class nutritionist who specializes in diabetes management. "
        "Please provide a personalized meal plan that can help me manage my blood sugar levels effectively."
    )

    response = generator(prompt, max_length=300, do_sample=True, temperature=0.7)
    return response[0]["generated_text"]

# Streamlit App
st.set_page_config(page_title="Diet Balance", page_icon="🥗", layout="centered")
st.title("Diet Balance")

st.write("""
**Diet Balance** is an AI-powered meal planning tool designed specifically for diabetic patients. 
By entering your sugar levels and dietary preferences, Diet Balance generates personalized meal plans 
to help manage blood sugar levels effectively.
""")

# Sidebar inputs
st.sidebar.header("Enter Your Details")

fasting_sugar = st.sidebar.number_input("Fasting Sugar Levels (mg/dL)", min_value=50, max_value=500, step=1)
pre_meal_sugar = st.sidebar.number_input("Pre-Meal Sugar Levels (mg/dL)", min_value=50, max_value=500, step=1)
post_meal_sugar = st.sidebar.number_input("Post-Meal Sugar Levels (mg/dL)", min_value=50, max_value=500, step=1)

dietary_preferences = st.sidebar.text_input("Dietary Preferences (e.g., vegetarian, low-carb)")

# Generate meal plan button
if st.sidebar.button("Generate Meal Plan"):
    with st.spinner("Generating your personalized meal plan..."):
        meal_plan = get_meal_plan(fasting_sugar, pre_meal_sugar, post_meal_sugar, dietary_preferences)
    st.subheader("Your Personalized Meal Plan:")
    st.markdown(meal_plan)

# Footer
st.markdown("<hr style='border: 2px solid black;'>", unsafe_allow_html=True)
st.write("© 2025 Adeel Munir | Made with ❤️ in Pakistan")
