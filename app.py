import streamlit as st
from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate

# FUNCTIONS


# UI
st.set_page_config(page_title='Blog Generation', page_icon="🤖", layout="centered", initial_sidebar_state="collapsed")

st.header("Generate Blogs")

input_text = st.text_input("Enter the blog topic")
col1, col2 = st.columns([5, 5])
with col1:
    no_of_words = st.number_input("No. of words", format='%d', min_value=0, max_value=4000)
with col2:
    blog_style = st.selectbox("Writing the blog for", ("Researcher", "Data Scientist", "Teachers", "Common people"),
                              index=0)

submit_button = st.button("Generate")

if submit_button:
    st.text("hello")
