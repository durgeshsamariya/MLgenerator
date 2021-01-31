import streamlit as st
import os
from sidebars import kNN_sidebar
from sidebars import LOF_sidebar
from sidebars import iForest_sidebar
import base64
from jinja2 import Environment, FileSystemLoader

def header(text):
    l = int((70 - len(text))/2)
    return "#" + '='*(l-1) + " " + text + " " + '='*l

def download_button(code, filename, text="Download (.py)"):
    # Reference: https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
    b64 = base64.b64encode(code.encode()).decode()
    href = f'<a download="{filename}" href="data:file/txt;base64,{b64}">{text}</a>'
    st.markdown(href, unsafe_allow_html=True)
# Page title.
st.title("Machine Learning Code Generator")
st.write("by Durgesh Samariya")
st.markdown("-----")

templates = {
    'Anomaly Detection': {
        'LOF': 'templates/Anomaly Detection/LOF',
        'iForest': 'templates/Anomaly Detection/iForest'
    },
    'Classification': {
        'kNN': 'templates/Classification/kNN'
    },
    'Clustering': {
        'DBSCAN': 'templates/Clustering/DBSCAN'
    }
}

with st.sidebar:
    st.write("## Choose Task")
    task = st.selectbox("Task", list(templates.keys()))
    if isinstance(templates[task], dict):
        algorithm = st.sidebar.selectbox(
            "Which Algorithm?", list(templates[task].keys())
        )
        template_path = templates[task][algorithm]
    else:
        template_path = templates[task]

    if algorithm == 'LOF':
        inputs = LOF_sidebar()
    if algorithm == "iForest":
        inputs = iForest_sidebar()

env = Environment(loader=FileSystemLoader(template_path), trim_blocks=True, lstrip_blocks=True)

template = env.get_template("code-template.py.jinja")
code = template.render(header=header, **inputs)

file_name = algorithm + ".py"
download_button(code, file_name)

st.code(code)