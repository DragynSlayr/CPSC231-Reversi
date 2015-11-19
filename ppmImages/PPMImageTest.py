import Converter

# Puts the pixels of the image in the specified file in a list.  The list returned
# is a 3D list: it contains rows of pixels where each pixel is a list of length three
# containing the values for red, green and blue intensity in order.
#
# The expected format of the file is simple PPM (P3) with the added restrictions that
# - The first line has only the string P3.
# - The second line has the height and width of the pixel raster.
# - The third line has the maximum colour intensity.
# - The remaining lines each represent a single row of pixel data.
# - There are no comments in the file.
#
# Parameters:
#     ppmImageFilename: string that has the full name of the file with the ppm image data.
# Returns:
#     3D list containing the pixel raster of the image.
# Errors:
#     If the file named ppmImageFilename does not exist or the data in the file does not
#     conform to our simplified PPM image file format, the program will return an empty list.
def getPixels(ppmImageFilename) :
    pixelsRaster = []
    try :
        ppmFile = open(ppmImageFilename,'r')
        #ignore first 3 lines in the ppm image file
        ppmFile.readline()
        ppmFile.readline()
        ppmFile.readline()

        # Go through the remaining lines in the file.  Each line is a row in
        # the raster.
        for line in ppmFile:
            # Each line contains all the numbers needed for the colours,  split to
            # get just the numbers.
            colourComponents = line.split()

            # Use these numbers to create a list of pixel data
            pixelRow = []

            # Each pixel is defined by three consecutive numbers.  For each iteration
            # in this loop, the index will point to the first number for a pixel.
            for index in range(0,len(colourComponents),3):
                # Each pixel has three numbers, one for red, one for green, one for blue.
                red = int(colourComponents[index])
                green = int(colourComponents[index+1])
                blue = int(colourComponents[index+2])

                # Add the data for this pixel to the row.
                pixelRow.append([red,green,blue])

            # We now have all the pixels for a row.  Add the row to the raster.
            pixelsRaster.append(pixelRow)

        ppmFile.close()
    except IOError :
        print("Encountered problem while reading data from " + ppmImageFilename)

    return pixelsRaster

# Checks if the colour specified by intensity of red, green and blue is a shade
# of green.  This assumes that red, green and blue intensity values are between
# 0 and 255.  In other words, this assumes that a colour is defined using 3 * 8 bits, or
# 24 bits.
def isGreen(red,green,blue) :
    red_range = 100 <= red <= 250
    green_range = 100 <= blue <= 250
    blue_range = 100 <= blue <= 250
    return red_range and green_range and blue_range

#Replaces any green pixels from foreground with background
#Params: foreground, A list containing the image to chromaKey
#        background, A list containing the image that will replace green in the foreground list
#Returns: A list that is a combination of foreground and background
#Notes: This function is pure, it will not modify foreground or background
def chromaKey(foreground, background) :
    #Create a copy of the foreground
    merged = foreground[:]

    #Traverse through the rows and pixel lists
    for row in range(len(foreground)):
        for pixel in range(len(foreground[row])):
            #Get the list of pixels for each location
            pixel_list = foreground[row][pixel]

            #Extract red, green and blue from the pixel
            red = pixel_list[0]
            green = pixel_list[1]
            blue = pixel_list[2]

            if isGreen(red, green, blue):
                #Only replace a pixel from the foreground if it is green
                merged[row][pixel] = background[row][pixel]

    #Return the merged list
    return merged

#Writes a ppm image to a file
#Params: filename, The name of the file to write to
#        image, A 3d list representing the ppm image
#Returns: None
#Errors: Will raise an exception if the image list is too short
def createPPMFile(filename, image) :
    if (len(image) < 1) :
        #Throw an error if the image list is empty
        raise IOError("Image list is empty!")
    else:
        #Open the file and write header data
        outfile = open(filename, "w")
        outfile.write("P3\n")
        outfile.write(str(len(image)) + " " + str(len(image[0])) + "\n")
        outfile.write("255\n")

        #Write each pixel to the file and format accordingly
        for row in image :
            for pixel in row :
                for colour in pixel :
                    outfile.write(str(colour) + " ")
            outfile.write("\n")
        outfile.close()

if __name__ == "__main__" :
    foregroundPixels = getPixels("Bird.ppm")
    backgroundPixels = getPixels("Sky.ppm")
    mergedPixels = chromaKey(foregroundPixels, backgroundPixels)
    createPPMFile("SkyInBird.ppm", mergedPixels)
    backgroundPixels = getPixels("SkyInBird.ppm")
    foregroundPixels = getPixels("BirdInSky.ppm")
    mergedPixels = chromaKey(foregroundPixels, backgroundPixels)
    createPPMFile("Beauty.ppm", mergedPixels)
