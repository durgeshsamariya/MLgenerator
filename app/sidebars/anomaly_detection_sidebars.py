import streamlit as st

DISTANCE_METRICS = {
    "Euclidean": "euclidean",
    "Manhattan": "manhattan"
}

SEARCH_ALGORITHM = {
    "Auto": "auto",
    "BallTree": "ball_tree",
    "KDTree": "kd_tree",
    "Brute-Force search": "brute"
}

ANOMALY_DETECTION_DATASETS = {
    "Glass": "glass",
    "Heart Disease": "heart_disease",
    "KDDCup99": "kddcup99",
    "Mnist": "mnist"
}

def kNN_ad_sidebar():
    inputs = {}
    with st.sidebar:
        st.write("## Input data")
        inputs["data"] = st.selectbox(
            "Which data set do you want to use?",
            ("Synthetic data", "Benchmark data"),
        )
        if inputs["data"] == "Synthetic data":
            inputs['contamination'] = st.number_input(
                "Contamination (percentage of outliers)", 0.0, None, 0.1, format="%f",
            )
            inputs['n_train'] = st.number_input(
                "number of training data points", 100, None, 200,
            )
            inputs['n_test'] = st.number_input(
                "number of testing data points", 50, None, 100,
            )
            inputs['n_features'] = st.number_input(
                "number of features in data set", 1, None, 2,
            )
        elif inputs["data"] == "Benchmark data":
            dataset = st.selectbox(
                "Which one?", list(ANOMALY_DETECTION_DATASETS.keys())
            )
            inputs["dataset"] = ANOMALY_DETECTION_DATASETS[dataset]
        st.write("## Model Hyperparameter")
        inputs['k'] = st.sidebar.number_input(
            "k?", 1, None, 10,
        )
        algo = st.selectbox(
            "Which nearest neighbor search algorithm do you want to use?",
            list(SEARCH_ALGORITHM.keys()),
        )
        inputs["search_algo"] = SEARCH_ALGORITHM[algo]
        dist = st.selectbox(
            "Which distance metric do you want to use?",
            list(DISTANCE_METRICS.keys()),
        )
        inputs["metric"] = DISTANCE_METRICS[dist]

        inputs["visualization_status"] = st.checkbox('Visualization?', False)
        if inputs["visualization_status"]:
            inputs["save"] = st.checkbox('Do you want to save the figure?', False)
    return inputs

def LOF_sidebar():
    inputs = {}
    with st.sidebar:
        st.write("## Input data")
        inputs["data"] = st.selectbox(
            "Which data set do you want to use?",
            ("Synthetic data", "Benchmark data"),
        )
        if inputs["data"] == "Synthetic data":
            inputs['contamination'] = st.number_input(
                "Contamination (percentage of outliers)", 0.0, None, 0.1, format="%f",
            )
            inputs['n_train'] = st.number_input(
                "number of training data points", 100, None, 200,
            )
            inputs['n_test'] = st.number_input(
                "number of testing data points", 50, None, 100,
            )
            inputs['n_features'] = st.number_input(
                "number of features in data set", 1, None, 2,
            )
        elif inputs["data"] == "Benchmark data":
            dataset = st.selectbox(
                "Which one?", list(ANOMALY_DETECTION_DATASETS.keys())
            )
            inputs["dataset"] = ANOMALY_DETECTION_DATASETS[dataset]
        st.write("## Model Hyperparameter")
        inputs['k'] = st.sidebar.number_input(
            "k?", 1, None, 10,
        )
        algo = st.selectbox(
            "Which nearest neighbor search algorithm do you want to use?",
            list(SEARCH_ALGORITHM.keys()),
        )
        inputs["search_algo"] = SEARCH_ALGORITHM[algo]
        dist = st.selectbox(
            "Which distance metric do you want to use?",
            list(DISTANCE_METRICS.keys()),
        )
        inputs["metric"] = DISTANCE_METRICS[dist]

        inputs["visualization_status"] = st.checkbox('Visualization?', False)
        if inputs["visualization_status"]:
            inputs["save"] = st.checkbox('Do you want to save the figure?', False)
    return inputs

def iForest_sidebar():
    inputs = {}
    with st.sidebar:
        st.write("## Input data")
        inputs["data"] = st.selectbox(
            "Which data set do you want to use?",
            ("Synthetic data", "Benchmark data"),
        )
        if inputs["data"] == "Synthetic data":
            inputs['contamination'] = st.number_input(
                "Contamination (percentage of outliers)", 0.0, None, 0.1, format="%f",
            )
            inputs['n_train'] = st.number_input(
                "number of training data points", 100, None, 200,
            )
            inputs['n_test'] = st.number_input(
                "number of testing data points", 50, None, 100,
            )
            inputs['n_features'] = st.number_input(
                "number of features in data set", 1, None, 2,
            )
        elif inputs["data"] == "Benchmark data":
            dataset = st.selectbox(
                "Which one?", list(ANOMALY_DETECTION_DATASETS.keys())
            )
            inputs["dataset"] = ANOMALY_DETECTION_DATASETS[dataset]
        st.write("## Model Hyperparameter")
        inputs['samples'] = st.number_input(
            "samples?", 2, None, 128,
        )
        inputs['trees'] = st.number_input(
            "trees?", 100, None, 100,
        )
        inputs["visualization_status"] = st.checkbox('Visualization?', False)
        if inputs["visualization_status"]:
            inputs["save"] = st.checkbox('Do you want to save the figure?', False)
    return inputs