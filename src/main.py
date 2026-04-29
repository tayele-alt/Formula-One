import os
import streamlit as st
import pandas as pd

APP_PATH = os.path.dirname(os.path.abspath(__file__))

def get_data_path(filename):
    return os.path.join(APP_PATH, "data", filename)
