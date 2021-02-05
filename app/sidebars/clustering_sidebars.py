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

def DBSCAN_sidebar():
    inputs = {}
    with st.sidebar:
        st.write("## Input data")
        inputs["data"] = st.selectbox(
            "Which data set do you want to use?",
            ("Synthetic data",),
        )
        if inputs["data"] == "Synthetic data":
            inputs['n_samples'] = st.number_input(
                "number of data points", 100, None, 1000,
            )
            inputs['n_features'] = st.number_input(
                "number of features in data set", 2, None, 2,
            )
            inputs['n_centers'] = st.number_input(
                "number of cluster centers", 3, None, 3,
            )
            inputs['cluster_std'] = st.number_input(
                "Cluster standard deviation", 0.1, None, 1.0, 
            )
        st.write("## Model Hyperparameter")
        inputs['eps'] = st.number_input(
            "epsilon?", 0.1, None, 0.5, step=0.1)
        inputs['min_samples'] = st.number_input(
            "Min Samples?", 1, None, 5,
        )
        dist = st.selectbox(
            "Which distance metric do you want to use?",
            list(DISTANCE_METRICS.keys()))
        inputs["metric"] = DISTANCE_METRICS[dist]
        algo = st.selectbox(
            "Which nearest neighbor search algorithm do you want to use?",
            list(SEARCH_ALGORITHM.keys()))
        inputs["search_algo"] = SEARCH_ALGORITHM[algo]
    return inputs

def KMEANS_sidebar():
    inputs = {}
    with st.sidebar:
        st.write("## Input data")
        inputs["data"] = st.selectbox(
            "Which data set do you want to use?",
            ("Synthetic data",),
        )
        if inputs["data"] == "Synthetic data":
            inputs['n_samples'] = st.number_input(
                "number of data points", 100, None, 1000,
            )
            inputs['n_features'] = st.number_input(
                "number of features in data set", 2, None, 2,
            )
            inputs['n_centers'] = st.number_input(
                "number of cluster centers", 3, None, 3,
            )
            inputs['cluster_std'] = st.number_input(
                "Cluster standard deviation", 0.1, None, 1.0, 
            )
        st.write("## Model Hyperparameter")
        inputs['n_centroids'] = st.number_input(
            "number of cluster/ number of centroids", 2, None, 3)
        inputs['max_iter'] = st.number_input(
            "Maximum number of interation to perform in single run?", 100, None, 300,
        )
    return inputs

def OPTICS_sidebar():
    inputs = {}
    with st.sidebar:
        st.write("## Input data")
        inputs["data"] = st.selectbox(
            "Which data set do you want to use?",
            ("Synthetic data",),
        )
        if inputs["data"] == "Synthetic data":
            inputs['n_samples'] = st.number_input(
                "number of data points", 100, None, 1000,
            )
            inputs['n_features'] = st.number_input(
                "number of features in data set", 2, None, 2,
            )
            inputs['n_centers'] = st.number_input(
                "number of cluster centers", 3, None, 3,
            )
            inputs['cluster_std'] = st.number_input(
                "Cluster standard deviation", 0.1, None, 1.0, 
            )
        st.write("## Model Hyperparameter")
        inputs['min_samples'] = st.number_input(
            "number of samples in neighborhood", 1, None, 5)
        dist = st.selectbox(
            "Which distance metric do you want to use?",
            list(DISTANCE_METRICS.keys()))
        inputs["metric"] = DISTANCE_METRICS[dist]
        algo = st.selectbox(
            "Which nearest neighbor search algorithm do you want to use?",
            list(SEARCH_ALGORITHM.keys()))
        inputs["search_algo"] = SEARCH_ALGORITHM[algo]
    return inputs