import pandas as pd

# Creating DataFrames:
amsterdam = pd.DataFrame({'date': ['2019-01-01', '2019-02-10', '2019-01-15'], 'ratings': ['Rainy', 'Cloud', 'Sunny']})
london = pd.DataFrame({'date': ['2019-01-05', '2019-01-01', '2019-04-10'], 'ratings': ['Cloud', 'Cloud', 'Sunny']})

print(amsterdam)
print(london)

# Merging ordered DataFrames:
weather = pd.merge_ordered(amsterdam, london)
print(weather)

# Merging ordered DataFrames so that the rows can be distinguished:
weather_suff = pd.merge_ordered(amsterdam, london, on='date', suffixes=['_ams', '_lon'])
print(weather_suff)

# Merging ordered DataFrames, using forward-filling to replace NaN entries with the most recent non-null entry:
weather_ffill = pd.merge_ordered(amsterdam, london, on='date', suffixes=['_ams', '_lon'], fill_method='ffill')
print(weather_ffill)