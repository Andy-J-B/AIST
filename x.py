# import yfinance as yf
# import os
# from datetime import datetime
# import json
# import pandas as pd
# import time

# import modules.data_module as db

# stock = yf.Ticker("SHOP.TO").history(period="20d", interval="1d")

# t = True

# # Set

# stock1 = "SHop"

# data1 = db.Data(stock1)
# ST1 = db.Set(data1.findData())


# data = db.Data(stock1)
# ST = db.Set(data.findData())
# newValue = ST.closeList()

d = {
    "set0": {
        "0": 75.69000244140625,
        "1": 75.8499984741211,
        "2": 75.9000015258789,
        "3": 75.75,
        "4": 75.94000244140625,
    },
    "set1": {
        "0": 76.05999755859375,
        "1": 76.01000213623047,
        "2": 76.05000305175781,
        "3": 75.91999816894531,
        "4": 75.9000015258789,
        "5": 75.87000274658203,
        "6": 75.91000366210938,
        "7": 75.77999877929688,
    },
    "set2": {
        "0": 75.45999908447266,
        "1": 75.68000030517578,
        "2": 75.76000213623047,
        "3": 75.96499633789062,
    },
}

l = [1, 2, 3]


loadedLength = len(d)

sets = d[f"set{loadedLength-1}"]

i = len(sets)

for set in l:
    sets[str(i)] = set

    i += 1

print(d)
