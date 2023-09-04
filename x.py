import yfinance as yf
import os
from datetime import datetime
import json
import pandas as pd
import time

import modules.data_module as db

SV = db.SigValues(1)
SV.sigfigRegression()
