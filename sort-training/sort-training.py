import pandas as pd

# Create DataFrame
weather = pd.DataFrame({'Month': ['Jan', 'Apr', 'Jul', 'Oct'], 'Mean TemperatureF': [32.1, 61.9, 68.9, 43.4]})

# Define index
weather1 = weather.set_index('Month')

# Print the head of weather1
print('DataFrame:')
print(weather1.head())

# Sort the index of weather1 in alphabetical order: weather2
weather2 = weather1.sort_index()

# Print the head of weather2
print('Alphabetical order:')
print(weather2.head())

# Sort the index of weather1 in reverse alphabetical order: weather3
weather3 = weather1.sort_index(ascending=False)

# Print the head of weather3
print('Reverse alphabetical order:')
print(weather3.head())

# Sort weather1 numerically using the values of 'Max TemperatureF': weather4
weather4 = weather1.sort_values('Mean TemperatureF')

# Print the head of weather4
print('Numerically order:')
print(weather4.head())
