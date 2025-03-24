import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import os

PATH = f'C:{os.sep}Users{os.sep}Natha{os.sep}Documents{os.sep}code{os.sep}GitHub{os.sep}codecademy_projects{os.sep}Data Analyst{os.sep}biodiversity_starter'
obs_df = pd.read_csv(os.path.join(PATH, 'observations.csv'), delimiter=',')
spec_df = pd.read_csv(os.path.join(PATH, 'species_info.csv'), delimiter=',')

# Data Wrangling

# print(obs_df.head())
# print(spec_df.head())
# print(obs_df.shape) # 23_296, 3
# print(spec_df.shape) # 5_824, 4
# print(obs_df.info()) # 0 null
# print(spec_df.info()) # conservation_status has 191 non null values
spec_df['conservation_status'] = spec_df['conservation_status'].fillna('Not Threatened')
def print_value_counts(df):
    df_cols = df.columns
    for col in df_cols:
        print(df[col].value_counts())
# print_value_counts(obs_df) # 4 parks with 5_824 entries each
# print_value_counts(spec_df)

# Merging

merged_df = pd.merge(obs_df, spec_df, on='scientific_name')
# print(merged_df.head(10))

# Variables

parks = obs_df['park_name'].unique()
categories = spec_df['category'].unique()
cons_status = spec_df['conservation_status'].unique()


# notes

# there seems to be 5,824 species in each park and there is at least one observation of each species in each park
# spec_df['conservation_status'] has 191 non null values, likely means all null values never gained conservation status and are okay
# set all spec_df['conservation_status'] null values to = 'Not Threatened'