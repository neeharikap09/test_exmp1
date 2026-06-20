from google import genai
import streamlit as st

# Create prompt template for generating state descriptions
description_template = "Give a short and informative description of the state {state_name}"

st.header("🗺️ State Description Generator")

st.subheader("❤️ Made by Build Fast with AI")

state_name = st.text_input("Enter State Name")

if st.button("Generate Description"):
    client = genai.Client(api_key=st.secrets['GOOGLE_API_KEY'])

    prompt = description_template.format(state_name=state_name)

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents=prompt
    )

    # Extract only text parts
    final_text = ""
    if response.candidates and response.candidates[0].content.parts:
        for part in response.candidates[0].content.parts:
            if hasattr(part, "text") and part.text:
                final_text += part.text

    st.write(final_text)
