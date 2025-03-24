import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ideas to investigate

# what species have the most observations
# what parks have the most observations of fish and amphibians
# what parks have the most endangered species
# what category has the most endangered species
# what category has the highest percentage of endangered species
# do endangered species have fewer observations than recovering species on average (probably have to look specifically at one category)

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

# What category of species has the most observations?

top_species = merged_df.groupby('category')['observations'].sum().sort_values(ascending=False)
sns.barplot(x=top_species.index, y=top_species.values, hue=top_species.index, palette='pastel')
plt.xlabel('Species')
plt.ylabel('Observations')
plt.title('Total observations of different species\nacross all four National Parks')
plt.xticks(rotation=30)
plt.ticklabel_format(style='plain', axis='y')
plt.show()
plt.close()

# What park has the most endangered species? (! Not Threatened)
# Species of Concern, Endangered, Threatened, In Recovery, Not Threatened

conservation_df = merged_df[merged_df['conservation_status'] != 'Not Threatened']
conservation = conservation_df.groupby('park_name')['observations'].sum().sort_values(ascending=False)
sns.barplot(x=conservation.index, y=conservation.values, hue=conservation.index, palette='pastel')
plt.xlabel('National Park')
plt.ylabel('Observations')
plt.title('Which National Park has the most sightings of any conservation species?')
plt.xticks(rotation=30)
plt.show()
plt.close()


# notes

# there seems to be 5,824 species in each park and there is at least one observation of each species in each park
# spec_df['conservation_status'] has 191 non null values, likely means all null values never gained conservation status and are okay
# set all spec_df['conservation_status'] null values to = 'Not Threatened'