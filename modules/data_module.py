# *** IMPORTS ***

import json, shutil, statistics, os
import yfinance as yf
from datetime import datetime


# *** CLASSES ***


# DATA CLASS


class Data:
    """Data class to Read, Edit and Remove Data"""

    # INITIATE VARIABLES
    def __init__(
        self,
        stockSymbol: str,
        period: str = "1d",
        interval: str = "2m",
        index: str = ".TO",
    ):
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

    def folderExists(self) -> bool:
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

    def fileExists(self) -> bool:
        date = datetime.today().strftime("%Y-%m-%d")
        fileBoolean = os.path.exists(f"stocks/{self.stockSymbol}/{date}.json")

        return fileBoolean

    # DATA FUNCTIONS

    def findData(self) -> dict:
        stock = yf.Ticker(self.stockSymbol + self.index).history(
            period=self.period, interval=self.interval
        )
        return stock

    def addData(self):
        date = datetime.today().strftime("%Y-%m-%d")
        data = self.makeData()

        with open(f"stocks/{self.stockSymbol}/{date}.json", "w") as file:
            json.dump(data, file)

    def makeData(self) -> dict:
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

    """Class that runs algorithms on sets, makes, polishes and classifies sets"""

    def __init__(self, data: dict):
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

    def closeValues(self) -> dict:
        dataDict = {}

        for i in range(len(self.data)):
            dataDict[f"{i}"] = self.data["Close"][i]

        return dataDict

    def closeList(self) -> dict:
        dataDict = []

        for i in range(len(self.data)):
            dataDict.append(self.data["Close"][i])

        return dataDict

    # REGRESSION LINE FUNCTIONS

    def subList(self, a: list, b: list) -> list:
        return a - b

    def productList(self, a: list, b: list) -> list:
        return a * b

    def addList(self, a: list, b: list) -> list:
        return a + b

    def regressionLine(self, y: list, outlier=False) -> list:
        x = self.numberlistRL(len(y), outlier)
        OLDY = y

        if outlier != False:
            newOutlier = reversed(
                list(map(self.subList, outlier, [1] * int(len(outlier))))
            )

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

    def numberlistRL(self, number: int, exempt=False) -> list:
        numberlist = []
        for numbers in range(int(number)):
            numberlist.append(numbers)

        if exempt != False:
            newexempt = list(map(self.subList, exempt, [1] * int(len(exempt))))
            for outliers in newexempt:
                numberlist.remove(outliers)

        final = list(map(self.addList, numberlist, [1] * int(len(numberlist))))
        return final

    def regressionLineDifference(self, NRL: float, ORL: float):
        PC = (abs((NRL - ORL)) / ORL) * 100.0

        print(NRL, ORL, PC)

        if 50 < abs(PC) < 100:
            return "outlier"
        elif abs(PC) >= 100:
            return "breakout"
        else:
            return True

    def setFirstORL(self):
        CL = self.closeList()
        RL = self.regressionLine(CL[0:4])
        with open("data/cleanUp.json", "w") as file:
            json.dump(RL[0], file)

    def setRL(self, RL: float):
        with open("data/cleanUp.json", "w") as file:
            json.dump(RL, file)

    # RESET FUNCTION

    def reset(self):
        with open("data/classification.json", "w") as file:
            pass
        with open("data/set.json", "w") as f:
            pass

    # CLEANER FUNCTION

    def newSet(self, setList: list):
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

    def extendPreviousSet(self, setList: list):
        with open("data/set.json", "r") as f:
            loaded = json.load(f)

        loadedLength = len(loaded)

        sets = loaded[f"set{loadedLength-1}"]

        i = len(sets)

        for set in setList:
            sets[str(i)] = set

            i += 1

        with open("data/set.json", "w") as f:
            json.dump(loaded, f)

    def addLastOutliers(self, outliers, i: int):
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

        return newOutliers[0]

    # Set Classification

    def makeClassification(self, direction: str):
        with open("data/classification.json", "r") as f:
            loaded = json.load(f)

        if str(loaded) != "{}":
            loadedLength = len(loaded)

            data = loaded

            data["set" + str(loadedLength)] = direction

            with open("data/classification.json", "w") as f:
                json.dump(data, f)
        else:
            data = {}

            data["set" + str(0)] = direction

            with open("data/classification.json", "w") as f:
                json.dump(data, f)

    def setClassification(self, ORL: float) -> str:
        if ORL > 0.00002:
            return "UPWARD"
        elif ORL < -0.00002:
            return "DOWN"
        else:
            return "LATERAL"

    def lastClassification(self):
        with open("data/classification.json", "r") as f:
            classificationDict = json.load(f)

        print(classificationDict)
        clist = []
        for values in classificationDict.values():
            clist.append(values)

        try:
            return clist[-1]
        except IndexError:
            return "Error"

    def polisher(self, classifiction: str, set: list, s: int, end: int) -> int:
        if classifiction == "UPWARD":
            return s + int(set.index(max(set))) + 1
        elif classifiction == "DOWN":
            return s + int(set.index(min(set))) + 1
        else:
            return end

    def cleanUp(self) -> list:
        t = True
        CL = self.closeList()
        CLLength = len(CL) - 1
        i = 5
        s = 0
        newS = 0

        outlierIndexes = False

        self.setFirstORL()

        while i < CLLength:
            if (i - s) > 3:
                with open("data/cleanUp.json", "r") as file:
                    ORL = json.load(file)

                if ORL == 0:
                    NewORL = self.regressionLine(CL[s:i], outlierIndexes)[0]
                    self.setRL(NewORL)

                else:
                    RL = self.regressionLine(CL[s:i], outlierIndexes)[0]  # NRL
                    PC = self.regressionLineDifference(RL, ORL)

                    if PC == "breakout" or (i - 3) > 9:
                        if outlierIndexes != False:
                            newS = self.addLastOutliers(outlierIndexes, i)

                        classification = self.setClassification(ORL)

                        if int(newS) != 0:
                            polishedEnd = self.polisher(
                                classification, CL[s:newS], s, newS
                            )
                            newS = 0

                        else:
                            polishedEnd = self.polisher(classification, CL[s:i], s, i)

                        previousClass = self.lastClassification()

                        if previousClass == classification:
                            self.extendPreviousSet(CL[s:polishedEnd])
                        else:
                            self.newSet(CL[s:polishedEnd])
                            self.makeClassification(classification)

                        i = polishedEnd
                        s = polishedEnd

                        self.setRL(0)

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


class SigValues(Set):
    """Child class of Set, SigValues makes 3 lists of significant figures"""

    def __init__(self, data: dict):
        super().__init__(data)

    def regressionLine(self, x: list, y: list) -> list:
        xMean = statistics.mean(x)
        yMean = statistics.mean(y)

        xSubMean = list(map(self.subList, x, [xMean] * int(len(x))))
        ySubMean = list(map(self.subList, y, [yMean] * int(len(y))))

        sxy = list(map(self.productList, ySubMean, xSubMean))
        sxx = list(map(self.productList, xSubMean, xSubMean))

        slope = sum(sxy) / sum(sxx)
        intercept = yMean - slope * xMean

        return [slope, intercept]

    def getData(self) -> list:
        with open("data/classification.json", "r") as cla:
            classData = json.load(cla)

        with open("data/set.json", "r") as se:
            setData = json.load(se)

        return [classData, setData]

    def sigfigmaker(self) -> list:
        d = self.getData()[1]
        c = self.getData()[0]

        i = 0

        sigfigs = {}
        sigfiglow = {}
        sigfighigh = {}
        s = 0

        for sets in d:
            for keys, values in d[sets].items():
                if keys == "0":
                    sigfigs[i] = values
                    if c[f"set{s}"] == "UPWARD":
                        sigfiglow[i] = values
                    if c[f"set{s}"] == "DOWN":
                        sigfighigh[i] = values
                elif keys == f"{len(sets)-1}":
                    sigfigs[i] = values
                    if c[f"set{s}"] == "DOWN":
                        sigfiglow[i] = values
                    if c[f"set{s}"] == "UPWARD":
                        sigfighigh[i] = values

                i += 1
            s += 1

        return [sigfigs, sigfiglow, sigfighigh]

    def sigfigRegression(self):
        sigfig = self.sigfigmaker()

        print(self.regressionLine(list(sigfig[0].keys()), list(sigfig[0].values())))
        print(self.regressionLine(list(sigfig[1].keys()), list(sigfig[1].values())))
        print(self.regressionLine(list(sigfig[2].keys()), list(sigfig[2].values())))
