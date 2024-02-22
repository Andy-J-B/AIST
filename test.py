import json
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


t = True

# Set

stock = ""
inputcsv = "read"
# dataType is False if only one interval, True if all historical data
ST1 = db.Set(inputcsv, 1)

print("START CLEAN UP")
clean = ST1.cleanUp()
outliers = clean[0]
intervals = clean[1]
specialClassChecker = clean[2]
direction = clean[3]

with open("data/set.json") as file:
    outputData = json.load(file)
    lastInterval = []
    lastInterval.append(
        outputData[f"{list(outputData)[-1]}"][
            list(outputData[f"{list(outputData)[-1]}"])[-1]
        ][-1]
    )
    lastInterval.append(list(outputData[f"{list(outputData)[-1]}"].keys())[-1])
    pass

exportToCSV(lastInterval, stock)

print("Done Clean Up \n\n")

while t == True:
    time.sleep(120)

    ST = db.Set(inputcsv, 0)
    data = [ST.dataOrganized[0][-1], ST.dataOrganized[1][-1], ST.dataOrganized[2][-1]]

    # If it's the first interval of a set
    if len(intervals[0]) == 0:
        print("0 Interval -> restart")
        # Find the direction of the first interval
        direction = ST.intervalDirection(data[1], data[2])
        # Add the intervals to the intervals list
        intervals[0].append(data[0])
        intervals[1].append(data[1])
        intervals[2].append(data[2])

        ST.addNewRegressionLine(
            ST.regressionLine(intervals[1] + intervals[2], intervals[0])[0]
        )

        continue

    newIntervalDirection = ST.intervalDirection(data[1], data[2])

    if newIntervalDirection != direction:
        outliers[0].append(data[0])
        outliers[1].append(data[1])
        outliers[2].append(data[2])
        specialClassChecker += 1

    # Add the new intervals to the intervals list
    else:
        intervals[0].append(data[0])
        intervals[1].append(data[1])
        intervals[2].append(data[2])
        specialClassChecker = 0

        # Add the new regression line to the file
        newRegressionLine = ST.regressionLine(
            intervals[1] + intervals[2], intervals[0]
        )[0]

    if len(intervals[0][0]) > 2:
        with open("data/regressionLine.json", "r") as f:
            oldRegressionLine = json.load(f)
        if ST.checkBreakout(newRegressionLine, oldRegressionLine):
            if direction == "UPWARD":
                # Get index of the max close value
                indexOfMax = intervals[2].index(max(intervals[2]))

                print("A")

                # Make and add the new set

                ST.newSet(
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

                newSetInformation = ST.cleanUp(newRemainingSet)

            elif direction == "DOWNWARD":
                # Get index of the max close value
                indexOfMin = intervals[2].index(min(intervals[2]))

                print("B")

                # Make and add the new set
                ST.newSet(
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
                newSetInformation = ST.cleanUp(newRemainingSet)

            outliers = newSetInformation[0]
            intervals = newSetInformation[1]
            specialClassChecker = newSetInformation[2]
            direction = newSetInformation[3]
            # Set RegressionLine in ST.V_Algorithm
            continue

    ST.addNewRegressionLine(newRegressionLine)
