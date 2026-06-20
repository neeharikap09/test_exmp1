from google import genai
import streamlit as st

# Prompt template
places_template = """
List the top places to visit in {state}.
For each place, provide:
1. Place Name
2. Short Description (2-3 sentences)

Format the response clearly.
"""

st.header("🌍 State Places Generator")

st.subheader("Find the best places to visit in any state")

state = st.text_input("Enter State Name")

if st.button("Generate Places"):
    client = genai.Client(api_key=st.secrets['GOOGLE_API_KEY'])

    prompt = places_template.format(state=state)

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents=prompt
    )

    # Extract only text parts
    final_text = ""
    if response.candidates and response.candidates[0].content.parts:
        for part in response.candidates[0].content.parts:
            if hasattr(part, 'text') and part.text:
                final_text += part.text

    st.write(final_text)
