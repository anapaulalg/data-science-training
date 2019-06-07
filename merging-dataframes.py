import pandas as pd

#Create DataFrames:
revenue = pd.DataFrame({'city': ['Paris', 'Amsterdam', 'London'], 'revenue': [1000, 590, 200]})
managers = pd.DataFrame({'city': ['Paris', 'Amsterdam', 'Madrid'], 'manager': ['Jhon', 'Jorge', 'Charles']})

print(revenue)
print(managers)

#Merging the DataFrames:
combined = pd.merge(revenue, managers, on='city')

print(combined)