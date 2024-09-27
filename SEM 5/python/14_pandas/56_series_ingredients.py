import pandas as pd

a = ["4 cups", "1 cup", "2 large", "1 can"]

data = pd.Series(a, index = ["Flour", "Milk", "Eggs", "Spam"])

print(data)