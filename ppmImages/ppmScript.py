import random
image = open("Apple.ppm", "r")
lines = image.readlines()
newImage = open("NewImage.ppm", "w")

for i in range(len(lines)):
    if i > 3:
        values = lines[i].split(" ")
        for j in range(len(values)):
            if values[j] != "\n":
                values[j] = str(int(values[j]) // 2)
        newLine = " ".join(values)
        newLine += "\n"
        newImage.write(newLine)
    else:
        newImage.write(lines[i])

image.close()
newImage.close()
