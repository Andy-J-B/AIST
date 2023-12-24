import yfinance as yf
import os
from datetime import datetime
import json
import pandas as pd
import time, statistics

import RIIS.modules.set as db

print("""\n\n\n\n\n\n\n\n\n\\n\n\n\n\n\n\n\n\n\n\n\n\n""")
data = yf.Ticker("SHOP.TO").history(period="3d", interval="2m")
# print(data)
dataDict = {}
Date = data.index.get_level_values("Datetime")
# print(str(Date[0]))
for i in range(len(data)):
    dataDict[str(Date[i])] = (data["Open"][i], data["Close"][i])

# data = {"1": (1, 2), "2": (3, 4), "3": (5)}
# print(data)

setClass = db.Set(dataDict)
setClass.cleanUp()
