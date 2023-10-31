import streamlit as st
from io import StringIO
from controllers.code_comparison_controller import search_code

MINIMUM_RESULT_LIMIT = 1
MAXIMUM_RESULT_LIMIT = 10


st.sidebar.markdown("# Code comparison")
st.sidebar.markdown("Compare a file of code with the whole database .")

st.markdown("# Code comparison")


uploaded_file = st.file_uploader("Insert a file of code here.")

if uploaded_file:
    with st.form("my_form"):
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        text_code = stringio.read()
        st.code(text_code)
        limit = st.number_input(
            "Number of results to retrieve:",
            MINIMUM_RESULT_LIMIT,
            MAXIMUM_RESULT_LIMIT,
            MINIMUM_RESULT_LIMIT,
        )

        submitted = st.form_submit_button("Get Comparisons")

    if submitted:
        response = search_code(uploaded_file, limit)
        st.markdown("## Code Similarities")
        for i, element in enumerate(response, 1):
            payload = element["payload"]
            score = round(element["score"] * 100, 6)
            st.markdown(
                f"""### {i}. {payload["file_name"]} : {score}%\n
Author: {payload["author"]}\n
Subject: {payload["subject"]}\n
Programming Language: {payload["code_language"]}\n
Date: {payload["date"]}\n
Lines of code: {payload["lines_of_code"]-1}"""
            )

            st.code(payload["text"])
