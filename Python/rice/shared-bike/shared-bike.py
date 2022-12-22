import pandas as pd

def read_csv(path):
    data = pd.read_csv(path)
    return data

data = read_csv(".\data\\bike_day.csv")
print(data)