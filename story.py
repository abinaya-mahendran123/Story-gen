import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AYOUR KEY")
model=genai.GenerativeModel("gemini-2.5-flash")
st.title("Story Spinner")
prompt=st.text_input("Enter your title")
a="you are a story generator, you will be given a topic you have to draft a story on that topic, include the tone adjustment.And give the story in the format of title, body and conclusion.Key features include genre selection  and characters"
if st.button("submit"):
    response=model.generate_content(a+prompt)
    st.write(response.text)