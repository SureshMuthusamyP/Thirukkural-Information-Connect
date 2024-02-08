import streamlit as st
import pandas as pd
from fuzzywuzzy import fuzz

path = "Data.csv"
df = pd.read_csv(path)

# Function to perform fuzzy search based on selected language
def search_thirukkural(user_entry, selected_language):
    # Convert user input to lowercase for case-insensitive search
    user_entry_lower = user_entry.lower()

    # Define the column based on the selected language
    if selected_language == 'தமிழ்':
        column_to_search = 'தமிழ்'
    elif selected_language == 'English':
        column_to_search = 'English'
    elif selected_language == 'हिन्दी':
        column_to_search = 'हिन्दी'
    else:
        st.error("Invalid language selection.")
        return pd.DataFrame()

    # Create a new DataFrame with fuzzy scores
    df_scores = df.copy()
    df_scores['Fuzzy_Score'] = df_scores[column_to_search].apply(lambda x: fuzz.ratio(x.lower(), user_entry_lower))

    # Set a threshold for matching
    threshold = 70

    # Check if any matches above the threshold
    if df_scores['Fuzzy_Score'].max() < threshold:
        st.warning("No matching Thirukkural found.")
        return pd.DataFrame()

    # Find the row with the highest fuzzy matching score above the threshold
    best_match = df_scores[df_scores['Fuzzy_Score'] > threshold].loc[df_scores['Fuzzy_Score'].idxmax()]

    return best_match