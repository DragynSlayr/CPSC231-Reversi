def incrementAllInFile(inputFile, outputFile):
    try:
        inFile = open(inputFile, "r")
        lines = inFile.readlines()
        inFile.close()

        toWrite = ""

        for i in range(len(lines)):
            lineSplit = lines[i].split()
            for j in range(len(lineSplit)):
                toWrite += str(int(lineSplit[j]) + 1) + " "

        outFile = open(outputFile, "w")
        outFile.write(toWrite)
        outFile.close()
    except Exception as e:
        open(outputFile, "w").close()

def main():
    incrementAllInFile("in.txt", "out.txt")

if __name__ == '__main__':
    main()
