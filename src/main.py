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




else:
    st.subheader("Select Teams to Compare")

    constructors = pd.read_csv(get_data_path("constructors.csv"))
    team_names = constructors["name"].tolist()
    selected_teams = st.multiselect("Pick up to 4 teams:", team_names, max_selections=4)

    if selected_teams:
        constructor_standings = pd.read_csv(get_data_path("constructor_standings.csv"))

        team_stats = []
        for team in selected_teams:
            constructor = constructors[constructors["name"] == team]
            constructor_id = constructor["constructorId"].values[0]

            team_races = len(results[results["constructorId"] == constructor_id])
            team_wins = len(results[(results["constructorId"] == constructor_id) & (results["position"] == "1")])

            last_races = races.groupby("year")["raceId"].max()
            team_champs = constructor_standings[
                (constructor_standings["constructor_id"] == constructor_id) &
                (constructor_standings["position"] == 1) &
                (constructor_standings["raceId"].isin(last_races))
            ]

            team_stats.append({
                "Teams": team,
                "Races": team_races,
                "Wins": team_wins,
            })
        st.dataframe(pd.DataFrame(team_stats))

if mode == "Drivers" and selected:
    driver_standings = pd.read_csv(get_data_path("driver_standings.csv"))

    stats = []
    for name in selected:
        
        first, last = name.split(" ", 1)
        driver = drivers[(drivers["forename"] == first) & (drivers["surname"] == last)]
        driver_Id = driver["driverId"].values[0]

        wins = len(results[(results["driverId"] == driver_Id) & (results["position"] == "1")])
        races_entered = len(results[results["driverId"] == driver_Id])

        last_races = races.groupby("year")["raceId"].max()
        champs = driver_standings[
                (driver_standings["driverId"] == driver_Id) & 
                (driver_standings["position"] == 1) &
                (driver_standings["raceId"].isin(last_races))
            ]["raceId"].count()

        stats.append({
            "Driver": name,
            "races": races_entered,
            "Wins": wins,
            "Championships": champs
        })
    
    st.dataframe(pd.DataFrame(stats))
    st.subheader("Wins Comparison")
    chart_data = pd.DataFrame(stats)
    st.bar_chart(chart_data.set_index("Driver")["Wins"])