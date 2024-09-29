import pandas as pd 

# download csv file from the given link 
# https://www.kaggle.com/datasets/christopheiv/winemagdata130k

df = pd.read_csv("winemag-data-130k-v2.csv")

print("\n1. Displaying row number 25:")
print("-" * 30)
print(df.iloc[25:26])
print("\n" + "-" * 30)
print("2. Displaying column number 13:")
print("-" * 30)
print(df.iloc[:, 13])
print("\n" + "-" * 30)
print("3. Displaying rows where country name is France:")
print("-" * 30)
print(df[df['country'] == 'France'])
print("\n" + "-" * 30)
print("4. Displaying records where province is Michigan and taster_name is Alexander Peartree:")
print("-" * 30)
print(df[(df['province'] == 'Michigan') & (df['taster_name'] == 'Alexander Peartree')])
print("\n" + "-" * 30)
print("5. Exploring describe() for the generated DataFrame:")
print("-" * 30)
print(df.describe(percentiles=None, include=None, exclude=None))
