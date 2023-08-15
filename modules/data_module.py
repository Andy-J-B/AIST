# IMPORTS


import yfinance as yf
import os
from datetime import datetime
import json
import shutil
import statistics
from scipy.stats import linregress
import numpy as np

# DATA CLASS


class Data:
    def __init__(self, stockSymbol, period="1d", interval="2m", index=".TO"):
        self.stockSymbol = stockSymbol
        self.period = period
        self.interval = interval
        self.index = index

    def mainDataFunction(self):
        folderBoolean = self.folderExists()
        fileBoolean = self.fileExists()

        if folderBoolean == True:
            if fileBoolean == True:
                self.editData()
            elif fileBoolean == False:
                self.makeFile()
                self.addData()
        elif folderBoolean == False:
            self.makeFolder()
            self.makeFile()
            self.addData()

    # FOLDER FUNCTIONS

    def makeFolder(self):
        os.mkdir(f"stocks/{self.stockSymbol}")

    def folderExists(self):
        folderBoolean = os.path.exists(f"stocks/{self.stockSymbol}")

        return folderBoolean

    def deleteFolder(self):
        if os.path.exists(f"stocks/{self.stockSymbol}"):
            shutil.rmtree(f"stocks/{self.stockSymbol}")

    # FILE FUNCTIONS

    def makeFile(self):
        date = datetime.today().strftime("%Y-%m-%d")
        newFile = open(f"stocks/{self.stockSymbol}/{date}.json", "x")
        newFile.close()

    def fileExists(self):
        date = datetime.today().strftime("%Y-%m-%d")
        fileBoolean = os.path.exists(f"stocks/{self.stockSymbol}/{date}.json")

        return fileBoolean

    # DATA FUNCTIONS

    def findData(self):
        stock = yf.Ticker(self.stockSymbol + self.index).history(
            period=self.period, interval=self.interval
        )
        return stock

    def addData(self):
        date = datetime.today().strftime("%Y-%m-%d")
        data = self.makeData()

        with open(f"stocks/{self.stockSymbol}/{date}.json", "w") as file:
            json.dump(data, file)

    def makeData(self):
        data = self.findData()

        dataDict = {}

        for i in range(len(data)):
            prices = {}
            prices["Open"] = data["Open"][i]
            prices["Close"] = data["Close"][i]
            prices["High"] = data["High"][i]
            prices["Low"] = data["Low"][i]
            prices["Volume"] = int(data["Volume"][i])

            dataDict[f"{i}"] = prices

        return dataDict

    def editData(self):
        date = datetime.today().strftime("%Y-%m-%d")
        data = self.makeData()

        open(f"stocks/{self.stockSymbol}/{date}.json", "w").close()

        with open(f"stocks/{self.stockSymbol}/{date}.json", "w") as file:
            json.dump(data, file)


# IMPORTS


# SET CLASS


class Set:
    def __init__(self, data):
        self.data = data

    # CHECKER FUNCTIONS

    def minimumValuesChecker(self):
        closeValues = len(self.closeValues())

        if closeValues > 4:
            return True
        elif closeValues < 4:
            return False
        elif closeValues == 4:
            return "equal"

    # VALUES FUNCTIONS

    def closeValues(self):
        dataDict = {}

        for i in range(len(self.data)):
            dataDict[f"{i}"] = self.data["Close"][i]

        return dataDict

    def closeList(self):
        dataDict = []

        for i in range(len(self.data)):
            dataDict.append(self.data["Close"][i])

        return dataDict

    # REGRESSION LINE FUNCTIONS

    def subList(self, a, b):
        return a - b

    def productList(self, a, b):
        return a * b

    def addList(self, a, b):
        return a + b

    def regressionLine(self, y, outlier=False):
        x = self.numberlistRL(len(y), outlier)
        OLDY = y

        if outlier != False:
            newOutlier = list(map(self.subList, outlier, [1] * int(len(outlier))))
            for outliers in newOutlier:
                y.remove(OLDY[outliers - 1])

        xMean = statistics.mean(x)
        yMean = statistics.mean(y)

        xSubMean = list(map(self.subList, x, [xMean] * int(len(x))))
        ySubMean = list(map(self.subList, y, [yMean] * int(len(y))))

        sxy = list(map(self.productList, ySubMean, xSubMean))
        sxx = list(map(self.productList, xSubMean, xSubMean))

        slope = sum(sxy) / sum(sxx)
        intercept = yMean - slope * xMean

        return [slope, intercept]

    def numberlistRL(self, number, exempt=False):
        numberlist = []
        for numbers in range(int(number)):
            numberlist.append(numbers)

        if exempt != False:
            newexempt = list(map(self.subList, exempt, [1] * int(len(exempt))))
            for outliers in newexempt:
                numberlist.remove(outliers)

        final = list(map(self.addList, numberlist, [1] * int(len(numberlist))))
        return final

    def regressionLineDifference(self, NRL, ORL):
        PC = (abs((NRL - ORL)) / ORL) * 100.0

        print(NRL, ORL, PC)

        if 150 < abs(PC) < 400:
            return "outlier"
        elif abs(PC) >= 400:
            return "breakout"
        else:
            return True

    # RESET FUNCTION

    def reset(self):
        with open("data/classification.json", "w") as file:
            pass
        with open("data/set.json", "w") as f:
            pass

    # CLEANER FUNCTION

    def newSet(self, setList):
        with open("data/set.json", "r") as f:
            loaded = json.load(f)

        if str(loaded) != "{}":
            loadedLength = len(loaded)

            sets = {}
            i = 0
            for set in setList:
                sets[str(i)] = set

                i += 1

            data = loaded

            data["set" + str(loadedLength)] = sets

            with open("data/set.json", "w") as f:
                json.dump(data, f)
        else:
            print("n")
            sets = {}
            i = 0
            for set in setList:
                sets[str(i)] = set

                i += 1

            data = {}

            data["set" + str(0)] = sets

            with open("data/set.json", "w") as f:
                json.dump(data, f)

    def setFirstORL(self):
        CL = self.closeList()
        RL = self.regressionLine(CL[0:4])
        with open("data/cleanUp.json", "w") as file:
            json.dump(RL[0], file)

    def newIndex(self, newS, i):
        if int(newS[0]) != 0:
            return newS[-1]
        else:
            return i

    def setRL(self, RL):
        with open("data/cleanUp.json", "w") as file:
            json.dump(RL, file)

    def addLastOutliers(self, outliers, i):
        l = sorted(outliers).pop()
        if l != (i - 1):
            return 0

        newOutliers = []

        for integer in outliers:
            if l in outliers:
                newOutliers.append(l)
            else:
                break
            l += -1

        return [newOutliers[-1], newOutliers[0]]

    def cleanUp(self):
        t = True
        CL = self.closeList()
        CLLength = len(CL) - 1
        i = 5
        s = 0
        newS = [0]
        end = 5

        outlierIndexes = False

        self.setFirstORL()

        while end < CLLength:
            end += 1
            if (i - s) > 3:
                with open("data/cleanUp.json", "r") as file:
                    ORL = json.load(file)

                if ORL == 0:
                    NewORL = self.regressionLine(CL[s:i], outlierIndexes)[0]
                    self.setRL(NewORL)

                else:
                    RL = self.regressionLine(CL[s:i], outlierIndexes)[0]  # NRL
                    PC = self.regressionLineDifference(RL, ORL)

                    if PC == "breakout":
                        if outlierIndexes != False:

                            newS = self.addLastOutliers(outlierIndexes, i)


                        if int(newS[0]) != 0:
                            self.newSet(CL[s : newS[-1]])
                            s = self.newIndex(newS, i)
                            newS = [0]

                        else:
                            self.newSet(CL[s:i])
                            s = i

                        ResetRL = 0
                        self.setRL(ResetRL)

                        outlierIndexes = False

                    elif PC == "outlier":
                        if outlierIndexes == False:
                            outlierIndexes = []
                        outlierIndexes.append(i - s)
                    else:
                        self.setRL(RL)

            i += 1
            print(outlierIndexes, s, i)
        
        return [s, i, outlierIndexes]
