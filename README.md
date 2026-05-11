# F1 Driver & Team Comparison Tool

## Description
An interactive dashboard for comparing Formula 1 drivers and constructors across history (1950-present). Users can analyze championships, race wins, and performance over time, and save custom comparisons to revisit later.

## How to Run
pip install streamlit pandas
streamlit run dist/main.py

## How to Use
1. Use the sidebar to switch between Drivers and Teams mode
2. Pick up to 4 drivers or teams from the dropdown
3. View the stats table and charts that appear
4. Type a name and hit Save to save your comparison
5. Use Load Comparison in the sidebar to reload a saved one

## File Structure
- README.md: this file
- src/: development code and data
- src/main.py: main app file
- src/data/: all CSV and JSON data files
- dist/: stable production version (this is what gets graded)
- dist/main.py: stable version of the app
- dist/data/: stable data files

## Data Source
Formula 1 World Championship Dataset from Kaggle

## AI Usage
AI was used to help debug errors and suggest fixes. All code was written and understood by me.