import streamlit as st
from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate


# ------------FUNCTIONS---------------
def get_response(text, words, style):
    llm = CTransformers(model="models/llama-2-7b-chat.ggmlv3.q8_0.bin", model_type="llama",
                        config={"max_new_tokens": 256, "temperature": 0.01})
    prompt = PromptTemplate.from_template(f"""write a blog for {style} on the topic {text} within {words} words.""")
    response = llm(prompt.format())
    print(response)
    return response


# -----------------------UI-------------------
st.set_page_config(page_title='Blog Generation', page_icon="🤖", layout="centered", initial_sidebar_state="collapsed")

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the blog topic")
col1, col2 = st.columns([5, 5])
with col1:
    no_of_words = st.number_input("No. of words", format='%d', min_value=0, max_value=4000)
with col2:
    blog_style = st.selectbox("Writing the blog for", ("Researcher", "Data Scientist", "Teachers", "Common people"),
                              index=0)

submit_button = st.button("Generate")

if submit_button:
    answer = get_response(input_text, no_of_words, blog_style)
    st.write(answer)
