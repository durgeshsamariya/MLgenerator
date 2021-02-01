import streamlit as st

DISTANCE_METRICS = {
    "Minkowski": "minkowski",
}

SEARCH_ALGORITHM = {
    "Auto": "auto",
    "BallTree": "ball_tree",
    "KDTree": "kd_tree",
    "Brute-Force search": "brute"
}

CLASSIFICATION_DATASETS = {
    "Diabetes": "diabetes",
    "Iris": "iris",
    "Pendigits": "pendigits"
}

KERNELS = {
    "RBF": 'rbf',
    "Linear": "linear",
    "Polynomial": "poly",
    "Sigmoid": "sigmoid"
}

PENALTY = {
    "L1": "l1",
    "L2": "l2",
    "Elastic Net": "elasticnet",
    "None": "none"
}

def kNN_sidebar():
    inputs = {}
    with st.sidebar:
        st.write("## Input data")
        inputs["data"] = st.selectbox(
            "Which data set do you want to use?",
            ("Synthetic data", "Benchmark data"),
        )
        if inputs["data"] == "Synthetic data":
            inputs['n_samples'] = st.sidebar.number_input(
                "number of data points", 100, None, 1000,
            )
            inputs['n_features'] = st.sidebar.number_input(
                "number of features in data set", 10, None, 10,
            )
            inputs['n_classes'] = st.sidebar.number_input(
                "number of classes", 2, None, 2,
            )
        elif inputs["data"] == "Benchmark data":
            dataset = st.selectbox(
                "Which one?", list(CLASSIFICATION_DATASETS.keys())
            )
            inputs["dataset"] = CLASSIFICATION_DATASETS[dataset]
        
        st.write("## Model Hyperparameter")
        inputs['k'] = st.sidebar.number_input(
            "k?", 1, None, 10,)
        algo = st.selectbox(
            "Which nearest neighbor search algorithm do you want to use?",
            list(SEARCH_ALGORITHM.keys()))
        inputs["search_algo"] = SEARCH_ALGORITHM[algo]
        dist = st.selectbox(
            "Which distance metric do you want to use?",
            list(DISTANCE_METRICS.keys()))
        inputs["metric"] = DISTANCE_METRICS[dist]

        inputs["visualization_status"] = st.checkbox('Visualization?', False)
        if inputs["visualization_status"]:
            inputs['plots'] = st.multiselect("What metrics to plot?", ('ROC Curve', 'Precision-Recall Curve'))
    return inputs

def SVM_sidebar():
    inputs = {}
    with st.sidebar:
        st.write("## Input data")
        inputs["data"] = st.selectbox(
            "Which data set do you want to use?",
            ("Synthetic data", "Benchmark data"),
        )
        if inputs["data"] == "Synthetic data":
            inputs['n_samples'] = st.sidebar.number_input(
                "number of data points", 100, None, 1000,
            )
            inputs['n_features'] = st.sidebar.number_input(
                "number of features in data set", 10, None, 10,
            )
            inputs['n_classes'] = st.sidebar.number_input(
                "number of classes", 2, None, 2,
            )
        elif inputs["data"] == "Benchmark data":
            dataset = st.selectbox(
                "Which one?", list(CLASSIFICATION_DATASETS.keys())
            )
            inputs["dataset"] = CLASSIFICATION_DATASETS[dataset]
        
        st.write("## Model Hyperparameter")
        inputs['C'] = st.number_input(
            "C (Regularization parameter)?", 1.00, 10.00, step = 0.01)
        kernel = st.selectbox(
            "Which kernel do you want to use?",
            list(KERNELS.keys()))
        inputs["kernel"] = KERNELS[kernel]
        if kernel == "Polynomial":
            inputs["degree"] = st.number_input(
                "Degree of Polynomial Kernel", 1, 10, 3
            )
        if (kernel == "RBF" or kernel == "Polynomial" or kernel == "Sigmoid"):
            inputs["gamma"] = st.selectbox("Gamma (Kernel Coefficient)", ("scale", "auto"))
        inputs["visualization_status"] = st.checkbox('Visualization?', False)
        if inputs["visualization_status"]:
            inputs['plots'] = st.multiselect("What metrics to plot?", ('ROC Curve', 'Precision-Recall Curve'))
    return inputs

def Logistic_Regression_sidebar():
    inputs = {}
    with st.sidebar:
        st.write("## Input data")
        inputs["data"] = st.selectbox(
            "Which data set do you want to use?",
            ("Synthetic data", "Benchmark data"),
        )
        if inputs["data"] == "Synthetic data":
            inputs['n_samples'] = st.sidebar.number_input(
                "number of data points", 100, None, 1000,
            )
            inputs['n_features'] = st.sidebar.number_input(
                "number of features in data set", 10, None, 10,
            )
            inputs['n_classes'] = st.sidebar.number_input(
                "number of classes", 2, None, 2,
            )
        elif inputs["data"] == "Benchmark data":
            dataset = st.selectbox(
                "Which one?", list(CLASSIFICATION_DATASETS.keys())
            )
            inputs["dataset"] = CLASSIFICATION_DATASETS[dataset]
        
        st.write("## Model Hyperparameter")
        penalty = st.selectbox(
            "Penalty", list(PENALTY.keys()))
        inputs["penalty"] = PENALTY[penalty]
        inputs['max_iter'] = st.number_input(
            "Maximum number of iterations", 100, 1000, 100)
        inputs["visualization_status"] = st.checkbox('Visualization?', False)
        if inputs["visualization_status"]:
            inputs['plots'] = st.multiselect("What metrics to plot?", ('ROC Curve', 'Precision-Recall Curve'))
    return inputs