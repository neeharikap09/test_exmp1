from google import genai
import streamlit as st

# Create prompt template for generating travel recommendations
places_template = """
List the top places to visit in {state_name}.
For each place, provide a short description.
Keep the response simple and easy to read.
"""

st.header("🗺️ State Travel Guide")

st.subheader("❤️ Made by Build Fast with AI")

state_name = st.text_input("Enter State Name")

if st.button("Generate Places to Visit"):
    client = genai.Client(api_key=st.secrets['GOOGLE_API_KEY'])

    prompt = places_template.format(state_name=state_name)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # Extract only text parts
    final_text = ""
    if response.candidates and response.candidates[0].content.parts:
        for part in response.candidates[0].content.parts:
            if hasattr(part, "text") and part.text:
                final_text += part.text

    st.write(final_text)
