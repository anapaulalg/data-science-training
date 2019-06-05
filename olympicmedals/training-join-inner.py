import pandas as pd

#Create DataFrames for top gold, silver and bronze:
gold = pd.DataFrame({'Country': ['United States', 'Soviet Union', 'United Kingdom', 'Italy', 'Germany'], 'Total': [2088, 838, 498, 460, 407]})
silver = pd.DataFrame({'Country': ['United States', 'Soviet Union', 'United Kingdom', 'France', 'Italy'], 'Total': [1195, 627, 591, 461, 394]})
bronze = pd.DataFrame({'Country': ['United States', 'Soviet Union', 'United Kingdom', 'France', 'Germany'], 'Total': [1052, 584, 505, 475, 454]})

#Def index
gold1 = gold.set_index('Country')
silver1 = silver.set_index('Country')
bronze1 = bronze.set_index('Country')

# Create the list of DataFrames: medal_list
medal_list = [bronze1, silver1, gold1]

# Concatenate medal_list horizontally using an inner join: medals
medals = pd.concat(medal_list, keys=['bronze1', 'silver1', 'gold1'], axis=1, join='inner')

# Print medals
print(medals)