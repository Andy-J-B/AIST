import yfinance as yf
import os
from datetime import datetime
import json
import pandas as pd
import time

import modules.data_module as db

sv = 50000
interest = float(0.2 / 100)

for i in range(252 * 5):
    sv = sv + sv * interest

    print(sv - 10000)

# SV = db.SigValues(1)
# SV.sigfigRegression()
