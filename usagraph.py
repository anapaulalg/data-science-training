import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read data
medals = pd.read_csv('Summer Olympic medallists 1896 to 2008 - ALL MEDALISTS.tsv', sep='\t')

medals.Medal = pd.Categorical(values=medals.Medal, categories=['Bronze', 'Silver', 'Gold'], ordered=True)

# Create the DataFrame: usa
usa = medals[medals.NOC == 'USA']

# Group usa by ['Edition', 'Medal'] and aggregate over 'Athlete'
usa_medals_by_year = usa.groupby(['Edition', 'Medal'])['Athlete'].count()

# Reshape usa_medals_by_year by unstacking
usa_medals_by_year = usa_medals_by_year.unstack(level='Medal')

# Plot the DataFrame usa_medals_by_year
usa_medals_by_year.plot()
usa_medals_by_year.plot.area()
plt.show()