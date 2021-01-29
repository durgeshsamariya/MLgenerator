import streamlit as st

def kNN_sidebar():
    inputs = {}
    with st.sidebar:
        inputs['k'] = st.sidebar.number_input(
            "k?", 1, None, 1000,
        )
        

def LOF_sidebar():
    inputs = {}
    with st.sidebar:
        inputs['k'] = st.sidebar.number_input(
            "k?", 1, None, 1000,
        )
        inputs["search_algo"] = st.selectbox(
            "Which nearest neighbor search algorithm do you want to use?",
            ("Auto", "BallTree", "KDTree", "Brute-Force search"),
        )
        inputs["metric"] = st.selectbox(
            "Which distance metric do you want to use?",
            ("Minkowski",),
        )

    return inputs
