import pandas as pd 
import os

# TODO: download csv file from the given link 
# * https://www.kaggle.com/datasets/christopheiv/winemagdata130k

dir = os.path.dirname(__file__)
file_path = os.path.join(dir, "data_file.csv")

df = pd.read_csv(file_path)

# ! 1:- Display row number 25

print("-" * 30)
print(df[25:26])   
print("\n" + "-" * 30)

# ! 2:- Displaying column number 13
print("-" * 30)
print(df.iloc[:, 13])
print("\n" + "-" * 30)

# ! 3:- Displaying rowa where country name is France
print("-" * 30)
print(df[df['country'] == 'France'])
print("\n" + "-" * 30)

# ! 4:- Displaying records where province is Michigan and taster_name is Alexander Peartree
print("-" * 30)
print(df[(df['province'] == 'Michigan') & (df['taster_name'] == 'Alexander Peartree')])
print("\n" + "-" * 30)

# ! 5. Exploring describe() for the generated DataFrame
print("-" * 30)
print(df.describe(percentiles=None, include=None, exclude=None))
