import streamlit as st
import os
from sidebars.anomaly_detection_sidebars import kNN_ad_sidebar
from sidebars.anomaly_detection_sidebars import LOF_sidebar
from sidebars.anomaly_detection_sidebars import iForest_sidebar
from sidebars.classification_sidebars import kNN_sidebar
from sidebars.classification_sidebars import SVM_sidebar
from sidebars.classification_sidebars import Logistic_Regression_sidebar
from sidebars.classification_sidebars import RF_sidebar
from sidebars.classification_sidebars import Decision_Trees_sidebar
from sidebars.clustering_sidebars import DBSCAN_sidebar
from sidebars.clustering_sidebars import KMEANS_sidebar
from sidebars.clustering_sidebars import OPTICS_sidebar
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
#st.write("by Durgesh Samariya")
"""
[![Star](https://img.shields.io/github/stars/durgeshsamariya/MLgenerator.svg?logo=github&style=social)](https://github.com/durgeshsamariya/MLgenerator/stargazers)
&nbsp[![GitHub issues](https://img.shields.io/github/issues/durgeshsamariya/MLgenerator.svg)](https://GitHub.com/durgeshsamariya/MLgenerator/issues/)
&nbsp[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
&nbsp[![Made With Love](https://img.shields.io/badge/Made%20With-Love-orange.svg)](https://github.com/chetanraj/awesome-github-badges) 
&nbsp[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee--yellow.svg?logo=buy-me-a-coffee&logoColor=orange&style=social)](https://www.buymeacoffee.com/themlphdstudent)

"""
st.markdown("-----")
"""

Generate your machine learning starter code in five simple steps. 

1. Select Task (Anomaly Detection or Classification or Clustering).
2. Select Algorithm
3. Specify data set and hyperparameters.
4. Starter code will be generated below.
5. Download the code.
"""
st.markdown("-----")


templates = {
    'Anomaly Detection': {
        'LOF': 'templates/Anomaly Detection/LOF',
        'iForest': 'templates/Anomaly Detection/iForest',
        'kNN': 'templates/Anomaly Detection/kNN'
    },
    'Classification': {
        'Logistic Regression': 'templates/Classification/Logistic Regression',
        'kNN': 'templates/Classification/kNN',
        'SVM': 'templates/Classification/SVM',
        'Random Forest': 'templates/Classification/Random Forest',
        'Decision Tree': 'templates/Classification/Decision Trees'
    },
    'Clustering': {
        'DBSCAN': 'templates/Clustering/DBSCAN',
        'K-Means': 'templates/Clustering/K-Means',
        'OPTICS': 'templates/Clustering/OPTICS',
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
    if task == "Anomaly Detection":
        if algorithm == 'LOF':
            inputs = LOF_sidebar()
        if algorithm == "iForest":
            inputs = iForest_sidebar()
        if algorithm == "kNN":
            inputs = kNN_ad_sidebar()
    if task == "Classification":
        if algorithm == "Logistic Regression":
            inputs = Logistic_Regression_sidebar()
        if algorithm == 'kNN':
            inputs = kNN_sidebar()
        if algorithm == 'SVM':
            inputs = SVM_sidebar()
        if algorithm == "Random Forest":
            inputs = RF_sidebar()
        if algorithm == "Decision Tree":
            inputs = Decision_Trees_sidebar()
    if task == "Clustering":
        if algorithm == "DBSCAN":
            inputs = DBSCAN_sidebar()
        if algorithm == "K-Means":
            inputs = KMEANS_sidebar()
        if algorithm == "OPTICS":
            inputs = OPTICS_sidebar()

env = Environment(loader=FileSystemLoader(template_path), trim_blocks=True, lstrip_blocks=True)

template = env.get_template("code-template.py.jinja")
code = template.render(header=header, **inputs)

file_name = task.replace(" ", "_") + "_" + algorithm.replace(" ", "_") + ".py"
download_button(code, file_name.lower())

st.code(code)