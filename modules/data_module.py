# Set Module
#
# set.py

# SET CLASS

# This file contains the set class
# Which is used for recieving data and forming it into a set


# Data should be formatted as :
# { <time>: ( <open>, <close> ), <time>: ( <open>, <close> ) }

# ***    Main Code    ***

# *** Imports
import json, statistics
import pandas as pd


# *** Classes
class Set:
    """Class that makes sets"""

    def __init__(self, csv: str, dataType: dict):
        self.csv = csv
        self.dataType = dataType
        self.data = self.dataFinder()
        # data organized as [[time][open][close]]
        self.dataOrganized = self.dataOrganizer()

    # DATA FUNCTIONS

    def dataFinder(self) -> list:
        csvLocation = self.csv

        with open(f"{csvLocation}.csv", "r") as file:
            listOfLines = file.read().splitlines()
            pass

        return listOfLines

    def dataOrganizer(self) -> list:
        """
        Organizes the data given to the class.
        Data recieved : []"open,close,time", "open,close,time"]
        Data exported : [ [ <time>, <time> ] [ <open>, <open> ], [ <close>, <close> ] ]
        """

        data = self.data

        dataOrganized = [[], [], []]
        for lines in data:
            words = lines.split(",")
            try:
                dataOrganized[0].append(words[2])
                dataOrganized[1].append(float(words[0]))
                dataOrganized[2].append(float(words[1]))
            except TypeError:
                dataOrganized[0].append(words[1])
                dataOrganized[1].append(float(words[0]))
                dataOrganized[2].append(float(words[0]))

        return dataOrganized

    # REGRESSION LINE FUNCTIONS

    def subList(self, a: list, b: list) -> list:
        return a - b

    def productList(self, a: list, b: list) -> list:
        return a * b

    def addList(self, a: list, b: list) -> list:
        return a + b

    def regressionLine(self, y: list, time: list, outlier=False) -> list:
        # print("RegressionLine - > ", y, time)
        x = self.numberlistRL(len(time), outlier)
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

        if sum(sxx) == 0:
            slope = 0
        elif (
            type(sum(sxy)) == int
            or type(sum(sxy)) == float
            or type(sum(sxy)) == int
            or type(sum(sxx)) == float
        ):
            slope = sum(sxy) / sum(sxx)
        else:
            slope = sum(sxy) / sum(sxx)

        # try:
        #     slope = sum(sxy) / sum(sxx)
        # except RuntimeWarning:
        #     print(sxy, sxx)
        # except ZeroDivisionError:
        #     slope = 0
        intercept = yMean - slope * xMean
        print([slope])
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

        if 400 < abs(PC):
            return True
        else:
            False

    def intervalDirection(self, open: float, close: float) -> str:
        if float(open) > float(close):
            return "DOWNWARD"
        elif float(close) > float(open):
            return "UPWARD"

    # CLEANER FUNCTION

    def newSet(self, intervals: list, special: bool = False):
        with open("data/set.json", "r") as f:
            loaded = json.load(f)

        # print("new Set->", intervals, special)

        if str(loaded) != "{}":
            loadedLength = len(loaded)

            sets = {}

            # { <time>: ( <open>, <close> ), <time>: ( <open>, <close> ) }
            sets[str(intervals[0][0])] = (intervals[1][0], intervals[2][0])
            if special:
                pass
            else:
                sets[str(intervals[0][-1])] = (intervals[1][-1], intervals[2][-1])

            data = loaded

            data["set" + str(loadedLength)] = sets

            with open("data/set.json", "w") as f:
                json.dump(data, f)
        else:
            sets = {}

            # { <time>: ( <open>, <close> ), <time>: ( <open>, <close> ) }
            sets[str(intervals[0][0])] = (intervals[1][0], intervals[2][0])
            if special:
                pass
            else:
                sets[str(intervals[0][-1])] = (intervals[1][-1], intervals[2][-1])

            data = {}

            data["set" + str(0)] = sets

            with open("data/set.json", "w") as f:
                json.dump(data, f)

    def oppositeDirection(self, previousDirection):
        if previousDirection == "UPWARD":
            return "DOWNWARD"
        elif previousDirection == "DOWNWARD":
            return "UPWARD"

    def checkBreakoutRule1(self, direction, currentInterval, firstInterval):
        if direction == "UPWARD":
            if currentInterval < firstInterval - firstInterval * 0.5:
                return True
        if direction == "DOWNWARD":
            if currentInterval > firstInterval + firstInterval * 0.5:
                return True
        return False

    def checkBreakout(self, NRL, ORL):
        PC = (abs((NRL - ORL)) / ORL) * 100.0
        if PC > 200:
            return True
        else:
            return False

    def checkBreakoutRule2(self, newRegressionLine):
        with open("data/regressionLine.json", "r") as f:
            oldRegressionLine = json.load(f)
        return self.regressionLineDifference(newRegressionLine, oldRegressionLine)

    def addNewRegressionLine(self, newRegressionLine):
        with open("data/regressionLine.json", "w") as file:
            json.dump(newRegressionLine, file)

    def cleanUp(self, data: list = False) -> list:
        """
        This function is used when you first start this program or if you reset it.
        It does whatever the main code runs but on the data of the last three days to organize the data and sets.
        """

        # Set variables
        if data != False:
            pass
        else:
            data = self.dataOrganized

        outliers = [[], [], []]
        intervals = [[], [], []]
        specialClassChecker = 0
        direction = None

        # Start for loop to find all the sets
        for interval in range(len(data[0])):
            # If it's the first interval of a set
            if len(intervals[0]) < 3:
                print("0 Interval -> restart")
                # Find the direction of the first interval
                direction = self.intervalDirection(data[1][interval], data[2][interval])
                # Add the intervals to the intervals list
                intervals[0].append(data[0][interval])
                intervals[1].append(data[1][interval])
                intervals[2].append(data[2][interval])
                print(intervals)
                self.addNewRegressionLine(
                    self.regressionLine(intervals[1] + intervals[2], intervals[0])[0]
                )
                print("REGRESSION LINE")
                print(self.regressionLine(intervals[1] + intervals[2], intervals[0])[0])

                continue

            newIntervalDirection = self.intervalDirection(
                data[1][interval], data[2][interval]
            )

            if newIntervalDirection != direction:
                outliers[0].append(data[0][interval])
                outliers[1].append(data[1][interval])
                outliers[2].append(data[2][interval])
                specialClassChecker += 1

            # Add the new intervals to the intervals list
            else:
                intervals[0].append(data[0][interval])
                intervals[1].append(data[1][interval])
                intervals[2].append(data[2][interval])
                specialClassChecker = 0

                # Add the new regression line to the file
                newRegressionLine = self.regressionLine(
                    intervals[1] + intervals[2], intervals[0]
                )[0]

            if len(intervals[0][0]) > 2:
                with open("data/regressionLine.json", "r") as f:
                    oldRegressionLine = json.load(f)
                print(oldRegressionLine, newRegressionLine)
                if self.checkBreakout(newRegressionLine, oldRegressionLine):
                    if direction == "UPWARD":
                        # Get index of the max close value
                        indexOfMax = intervals[2].index(max(intervals[2]))

                        print("A")

                        # Make and add the new set

                        self.newSet(
                            [
                                intervals[0][0 : indexOfMax + 1],
                                intervals[1][0 : indexOfMax + 1],
                                intervals[2][0 : indexOfMax + 1],
                            ]
                        )

                        # run algorithm on the set that remains
                        newRemainingSet = [
                            intervals[0][indexOfMax + 1 :],
                            intervals[1][indexOfMax + 1 :],
                            intervals[2][indexOfMax + 1 :],
                        ]

                        newSetInformation = self.cleanUp(newRemainingSet)

                    elif direction == "DOWNWARD":
                        # Get index of the max close value
                        indexOfMin = intervals[2].index(min(intervals[2]))

                        print("B")

                        # Make and add the new set
                        self.newSet(
                            [
                                intervals[0][0 : indexOfMin + 1],
                                intervals[1][0 : indexOfMin + 1],
                                intervals[2][0 : indexOfMin + 1],
                            ]
                        )

                        # run algorithm on the set that remains
                        newRemainingSet = [
                            intervals[0][indexOfMin + 1 :],
                            intervals[1][indexOfMin + 1 :],
                            intervals[2][indexOfMin + 1 :],
                        ]

                        print("Start V-Alg")
                        newSetInformation = self.cleanUp(newRemainingSet)

                    outliers = newSetInformation[0]
                    intervals = newSetInformation[1]
                    specialClassChecker = newSetInformation[2]
                    direction = newSetInformation[3]
                    # Set RegressionLine in self.V_Algorithm
                    continue

            self.addNewRegressionLine(newRegressionLine)

        return [outliers, intervals, specialClassChecker, direction]
