import json

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
        writer_object.writerow("\n")

        # Close the file object
        f_object.close()
    return


exportToCSV(lastInterval[0], lastInterval[1])
