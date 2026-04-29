import os
import streamlit as st
import pandas as pd

APP_PATH = os.path.dirname(os.path.abspath(__file__))

def get_data_path(filename):
    return os.path.join(APP_PATH, "data", filename)

@st.cache_data
def load_drivers():
    df = pd.read.csv(get_data_path("drivers.csv"))
    return df

@st.cache.data
def load_results():
    df = pd.read_cvs(get_data_path("results.cvs"))
    return df

@st.cache.data
def load_constructor_standing():
    df = pd.read_csv(get_data_path("constructor_standings.cvs"))
    return df