# IMPORTS
import json, statistics
import numpy as np
from scipy.stats import linregress

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

    def numberlist(self, number):
        numberlist = []
        for numbers in range(int(number)):
            numberlist.append(numbers)
        return numberlist

    def regressionLine(self, list):
        Closelist = list

        numberslist = self.numberlist(len(Closelist))
        lineregress = linregress(numberslist, Closelist)

        A = lineregress.intercept
        B = lineregress.slope

        x = Closelist
        xvalues = self.numberlist(len(x))

        ylist = []

        for xamnt in x:
            sdy = statistics.stdev(x)
            sdx = statistics.stdev(xvalues)
            meany = statistics.mean(Closelist)
            meanx = statistics.mean(xvalues)
            r = np.corrcoef(xvalues, x)

            B = r[0, 1] * (sdy / sdx)
            A = meany - B * meanx
            yhat = A + B * xamnt
            ylist.append(yhat)

        returnValues = []
        returnValues.append(x)
        returnValues.append(ylist)

        lengthX = self.numberlist(len(returnValues[0]))

        slope = linregress(lengthX, ylist).slope

        return slope

    def regressionLineDifference(self, NRL, ORL):
        PC = (abs((NRL - ORL)) / ORL) * 100.0

        print(NRL, ORL, PC)

        if 150 < PC < 400:
            return "outlier"
        elif PC >= 400:
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
            json.dump(RL, file)

    def newIndex(self, s, i):
        return i

    def cleanUp(self):
        t = True
        CL = self.closeList()
        CLLength = len(CL) - 1
        i = 5
        s = 0
        end = 5

        self.setFirstORL()

        while end < CLLength:
            end += 1
            if (i - s) > 3:
                with open("data/cleanUp.json", "r") as file:
                    ORL = json.load(file)

                if ORL == 0:
                    NewORL = self.regressionLine(CL[s:i])
                    with open("data/cleanUp.json", "w") as file:
                        json.dump(NewORL, file)

                else:
                    RL = self.regressionLine(CL[s:i])  # NRL
                    PC = self.regressionLineDifference(RL, ORL)

                    if PC == "breakout":
                        self.newSet(CL[s:i])
                        s = self.newIndex(s, i)
                        ResetRL = 0

                        with open("data/cleanUp.json", "w") as file:
                            json.dump(ResetRL, file)

                    elif PC == "outlier":
                        pass
                    else:
                        with open("data/cleanUp.json", "w") as file:
                            json.dump(RL, file)

            i += 1
            print(s, i, CL[i], end)