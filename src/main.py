import os
import streamlit as st
import pandas as pd

APP_PATH = os.path.dirname(os.path.abspath(__file__))

def get_data_path(filename):
    return os.path.join(APP_PATH, "data", filename)

st.title("F1 Driver & Team Comparison")
st.markdown("Compare F1 drivers and teams across history")

st.sidebar.header("Settings")
mode = st.sidebar.radio("Compare by", ["Drivers", "Teams"])

@st.cache_data
def load_drivers():
    df = pd.read_csv(get_data_path("drivers.csv"))
    return df

@st.cache_data
def load_results():
    df = pd.read_csv(get_data_path("results.csv"))
    return df

@st.cache_data
def load_races():
    df = pd.read_csv(get_data_path("races.csv"))
    return df

drivers = load_drivers()
results = load_results()
races = load_races()

if mode == "Drivers":
    st.subheader("Select Drivers to Compare")
    driver_name = drivers["forename"] + " " + drivers["surname"]
    selected = st.multiselect("Pick up to 4 drivers:", driver_name, max_selections=4)


    if selected:
        st.write("You selected:", selected)

else:
    st.subheader("Constructors Data")
    st.dataframe(drivers)

driver_standings = pd.read_csv(get_data_path("driver_standings.csv"))

stats = []
for name in selected:
    first, last = name.split(" ", 1)
    driver = drivers[(drivers["forename"] == first) & (drivers["surname"] == last)]
    driver_Id = driver["driverId"].values[0]

    wins = len(results[results["driverId"] == driver_Id]) & (results["position"] == "1")
    races_entered = len(results[results["driverId"] == driver_Id])

    stats.append({
        "Driver": name,
        "races": races_entered,
        "Wins": wins
    })

st.dataframe(pd.DataFrame(stats))