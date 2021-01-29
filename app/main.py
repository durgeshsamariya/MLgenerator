import streamlit as st
import os
from sidebars import kNN_sidebar
from sidebars import LOF_sidebar
from jinja2 import Environment, FileSystemLoader

# Set page title.
st.title("Machine Learning Code Generator")

#templates = collections.defaultdict(dict)
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

#with st.sidebar:
st.sidebar.write("## Choose Task")
task = st.sidebar.selectbox("Task", list(templates.keys()))
if isinstance(templates[task], dict):
    algorithm = st.sidebar.selectbox(
        "Which Algorithm?", list(templates[task].keys())
    )
    template_path = templates[task][algorithm]
else:
    template_path = templates[task]

st.sidebar.write("### Hyperparameters")
#print(algorithm)
if algorithm == 'LOF':
    inputs = LOF_sidebar()

#if algorithm == 'kNN':
#    kNN_sidebar()

st.sidebar.write("### Pre-processing")
preprocess = st.sidebar.radio("Choose Scaler", ("StandardScaler: Scale to 0 mean and 1 standard deviation", "MinMaxScaler: Convert all values in the columns from 0 to 1"), key = 'preprocess')

env = Environment(
    loader=FileSystemLoader(template_path), trim_blocks=True, lstrip_blocks=True,
)
template = environment.get_template("code-template.py.jinja")
code = template.render(notebook=False, **inputs)

st.code(code)

#sidebar_input = template_specific_sidebar.show()

#st.sidebar.subheader("Choose Classifier")
#classifier = st.sidebar.selectbox("Classifier", ("Support Vector Machine (SVM)", "Logistic Regression", "Random Forest"))