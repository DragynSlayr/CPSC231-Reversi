#Gets the pixels from a file, in a 3d list
#Params: file_name, The name of the file
#Returns: A 3d list containing each pixel and it's color data
def getPixels(file_name):
    #Open the file in reading mode
    image_file = open(file_name, "r")

    #Read all the lines of the file
    lines = image_file.readlines()

    #Close the file since we are finished with it
    image_file.close()

    #This list will hold each row of the file
    row = []

    #This list holds all lines of the file
    image_info = []

    #Go through the lines from the file
    for i in range(len(lines)):

        #Skip the first three lines, as they have no pixel values
        if i > 2:
            #Split the line into each rgb value
            values = lines[i].split()

            #This list will hold each pixel
            pixel = []

            for value in values:
                if len(pixel) == 2:
                    #Add the final value to pixel
                    pixel.append(value)

                    #Add the pixel info to the row once we have R G and B
                    row.append(pixel)

                    #Check the size of row to see if it is full
                    if len(row) == 4:
                        #Add the row to the image info, then clear the row
                        image_info.append(row)
                        row = []

                    #Clear the pixel
                    pixel = []
                else:
                    #Add the value to the pixel list since we don't have R G and B
                    pixel.append(value)

    #Return the 3 dimensional list
    return image_info

#Testing
def main():
    print(getPixels("feep.ppm"))

if __name__ == "__main__":
    main()
