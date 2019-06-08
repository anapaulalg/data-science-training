import pandas as pd

# Creating DataFrames:
revenue = pd.DataFrame({'city': ['Paris', 'Amsterdam', 'London'], 'revenue': [1000, 590, 200]})
managers = pd.DataFrame({'city': ['Paris', 'Amsterdam', 'Madrid'], 'manager': ['Jhon', 'Jorge', 'Charles']})

# Changing index:
revenue1 = revenue.set_index('city')
managers1 = managers.set_index('city')

print(revenue1)
print(managers1)

# Joining DataFrames (the output with the 3 citys and NaN in manager London):
join_left = revenue1.join(managers1)
print(join_left)

# Joining DataFrames (output with the 3 citys and NaN in revenue Madrid):
join_right = revenue1.join(managers1, how='right')
print(join_right)
