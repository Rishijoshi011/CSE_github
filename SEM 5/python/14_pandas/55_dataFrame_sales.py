import pandas as pd

a = {
    "Apple" : [35, 21],
    "Banana" : [41, 34]
}

data = pd.DataFrame(a, index = ["2017 Sales", "2018 Sales"])

print(data)