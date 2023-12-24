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

stock1 = "shop"

data1 = db.Data(stock1, "14d", "15m")
ST1 = db.Set(data1.findData())
MVC1 = ST1.minimumValuesChecker()

if MVC1 == True:
    clean = ST1.cleanUp()
    s = clean[0]
    i = clean[1]
    outlierIndexed = clean[2]
    newS = 0

    print("Done Clean Up \n\n")

    while t == True:
        time.sleep(120)

        data = db.Data(stock1)
        ST = db.Set(data.findData())
        CL = ST.closeList()

        if (i - s) > 3:
            with open("data/cleanUp.json", "r") as file:
                ORL = json.load(file)

            if ORL == 0:
                NewORL = ST.regressionLine(CL[s:i], outlierIndexes)[0]
                ST.setRL(NewORL)

            else:
                RL = ST.regressionLine(CL[s:i], outlierIndexes)[0]  # NRL
                PC = ST.regressionLineDifference(RL, ORL)

                if PC == "breakout" or (i - 3) > 9:
                    if outlierIndexes != False:
                        newS = ST.addLastOutliers(outlierIndexes, i)

                    classification = ST.setClassification(ORL)

                    if int(newS) != 0:
                        polishedEnd = ST.polisher(classification, CL[s:newS], s, newS)
                        newS = 0

                    else:
                        polishedEnd = ST.polisher(classification, CL[s:i], s, i)

                    previousClass = ST.lastClassification()

                    if previousClass == classification:
                        ST.extendPreviousSet(CL[s:polishedEnd])
                    else:
                        ST.newSet(CL[s:polishedEnd])
                        ST.makeClassification(classification)

                    s = polishedEnd
                    i = polishedEnd

                    ST.setRL(0)

                    outlierIndexes = False

                elif PC == "outlier":
                    if outlierIndexes == False:
                        outlierIndexes = []
                    outlierIndexes.append(i - s)
                else:
                    ST.setRL(RL)

        i += 1
        print(outlierIndexes, s, i)
