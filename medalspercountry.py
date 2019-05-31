import pandas as pd
import numpy as np

#Read data
medals = pd.read_csv('Summer Olympic medallists 1896 to 2008 - ALL MEDALISTS.tsv', sep='\t')

# Select the 'NOC' column of medals: country_names
country_names = medals['NOC']

# Count the number of medals won by each country: medal_counts
medal_counts = country_names.value_counts()

# Print top 11 countries ranked by medals
print(medal_counts.head(11))

# Construct the pivot table: counted
counted = medals.pivot_table(index='NOC', values='Athlete', columns= 'Medal', aggfunc='count')

# Create the new column: counted['totals']
counted['totals'] = counted.sum(axis='columns')

# Sort counted by the 'totals' column
counted = counted.sort_values('totals', ascending=False)

# Print the top 11 rows of counted
print(counted.head(11))