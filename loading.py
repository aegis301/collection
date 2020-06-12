from csv import reader

with open("Artworks_short.csv") as csvFile:
    stream = reader(csvFile)

    streamList = list(stream)

    # remove first line of dataset
    streamList = streamList[1:]

    for i in streamList:
        print(i)
