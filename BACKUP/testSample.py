import yfinance as yf
import os
from datetime import datetime
import json
import pandas as pd
import time


import modules.data_module as db
from csv import writer


def exportToCSV(data, file):
    # List that we want to add as a new row
    List = [data[0], data[1]]

    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open(f"{file}.csv", "a") as f_object:

        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)

        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(List)

        # Close the file object
        f_object.close()
    return


stock = yf.Ticker("SHOP.TO").history(period="3d", interval="2m")

t = True

# Set

stock1 = "shop"

data1 = db.Data(stock1, "3d", "2m")
ST1 = db.Set(data1.findData())
MVC1 = ST1.minimumValuesChecker()

if MVC1 == True:
    print("START CLEAN UP")
    clean = ST1.cleanUp()
    s = clean[0]
    i = clean[1]
    outlierIndexed = clean[2]
    exportToCSV(clean, stock1)

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
                NewORL = ST.regressionLine(ST.twoValueRL(CL, s, i, outlierIndexes))[0]
                ST.setRL(NewORL)

            else:
                RL = ST.regressionLine(ST.twoValueRL(CL, s, i, outlierIndexes))[
                    0
                ]  # NRL
                PC = ST.regressionLineDifference(RL, ORL)

                if PC == "breakout" or (i - 3) > 9:
                    classification = ST.setClassification(ORL)
                    polishedEnd = ST.polisher(classification, CL, s, i)

                    previousClass = ST.lastClassification()

                    if previousClass == classification:
                        ST.extendPreviousSet(CL, s, polishedEnd)
                        i = polishedEnd
                        s = polishedEnd
                        outlierIndexes = False

                        ST.setRL(0)

                    elif classification == "UPWARD":
                        newI = ST.findMaxI(i, s, outlierIndexes)
                        ST.newSet(s, polishedEnd)
                        ST.makeClassification(classification)

                        results = ST.vTheorem(polishedEnd, i)

                        i = results[0]
                        s = results[1]
                        outlierIndexes = results[2]

                    elif classification == "DOWN":
                        newI = ST.findMinI(i, s, outlierIndexes)
                        ST.newSet(s, polishedEnd)
                        ST.makeClassification(classification)

                        results = ST.vTheorem(polishedEnd, i)

                        i = results[0]
                        s = results[1]
                        outlierIndexes = results[2]

                elif PC == "outlier":
                    if outlierIndexes == False:
                        outlierIndexes = []
                    outlierIndexes.append(i - s)
                else:
                    ST.setRL(RL)

        i += 1
        print(outlierIndexes, s, i)
