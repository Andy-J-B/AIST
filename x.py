import yfinance as yf
import os
from datetime import datetime
import json
import pandas as pd
import time

import modules.data_module as db

stock = yf.Ticker("SHOP.TO").history(period="20d", interval="1d")

t = True

# Set

stock1 = "SHop"

data1 = db.Data(stock1)
ST1 = db.Set(data1.findData())


data = db.Data(stock1)
ST = db.Set(data.findData())
newValue = ST.closeList()
