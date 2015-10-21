import TurtleMove
import string
import Constants
import ReversiGrid


#Function returns a string that represents the initial grid state
#Takes no parameters
def initialize_grid_string_start():
	l_gridState = 'NNNNNNNNNNNNNNNNNNNNNNNNNNNBWNNNNNNWBNNNNNNNNNNNNNNNNNNNNNNNNNNN'
	return l_gridState
	
	
#Function takes a string and a location and returns the char at the loction
def get_Char(P_string, P_location):
	#print(P_location, "in", P_string)
	l_location = P_string[P_location-1]
	return l_location
	
	
	

#Function checks if a location is on the board
#Function takes the current grid string and an unstripped location string
#Returns Boolean whether or not it is on the grid.
def validate_move_location(P_gridString, P_location):
	L_xy = TurtleMove.get_column_and_row(P_location)
	L_x =  convert_column_number(L_xy[0]) #NOTE!!: This will be assigned 'invalid_range' if it is outside of range. This is done by the convert function
	L_y = L_xy[1]
	print (L_x)
	print(L_y)
	
	#Check if the location is on the board, 
	if L_x == 'invalid_range':
		print(L_y)
		print("x out of Range")
		return False
	
	if 0<= L_y > 8:
		print ("y out of range")
		return False
	
	
	
	#Checks if the location is occupied already
	if 'U' != get_Char(P_gridString, L_x + (8*(L_y -1))):
		#All of that math simply takes the number of x + a certain number of rows
		return False
	
	#If the location is on the board return True.
	return True
	
	
def convert_column_number(column):
	columnAll = 'ABCDEFGH'
	loopcount = 0
	for letter in columnAll:
		if column == letter:
			return loopcount +1
		loopcount = loopcount +1
		
	#print (column)
	return 'invalid_range'
	
	
#Function checks if move is beside a piece of the other colour
#Function takes the current grid string and an unstripped location string, as well as the colour being placed
#Returns Boolean depending on the local pieces
	# - By local, it referes the pieces of in the immediate vicinity to the location on the grid
def validate_local_location(P_gridString, P_location, colour):
	
	
	
	L_xy = TurtleMove.get_column_and_row(P_location)
	L_x =  convert_column_number(L_xy[0]) #NOTE!!: This will be assigned 'invalid_range' if it is outside of range. This is done by the convert function
	#Subtract one to bring it so 1 = 0, which simplifies later calulations
	L_y = L_xy[1]-1
	L_StringLocation = L_y*8 + L_x
	 
	#########
	#|1|2|3|#
	#|4|x|5|#
	#|6|7|8|#	
	#########
	
	
	
	
	#These locations will then be compared to what is stored in the string to check if any of the pieces is of the opposite colour 
	
	L_gridSpot1 = L_StringLocation -9
	L_gridSpot2 = L_StringLocation -8	
	L_gridSpot3 = L_StringLocation -7
	L_gridSpot4 = L_StringLocation -1
	L_gridSpot5 = L_StringLocation +1
	L_gridSpot6 = L_StringLocation +7
	L_gridSpot7 = L_StringLocation +8
	L_gridSpot8 = L_StringLocation +9
	
	loopcount = 0
	L_gridList=[L_gridSpot1,  L_gridSpot2, L_gridSpot3,  L_gridSpot4, L_gridSpot5, L_gridSpot6, L_gridSpot7, L_gridSpot8 ]
	for L_gridSpot in L_gridList:
		
	#	print (L_gridSpot)
	#	print(L_gridSpot <0)
		
		if L_gridSpot <= 0:
			L_gridList[loopcount] = 'U'
	#		print("done")
		
		if L_gridSpot >=64:
			L_gridList[loopcount] = 'U'
			
		if L_gridSpot%8 == 1:
			L_gridList[loopcount ] = 'U'
			########################################################################
			#This is not correctly detecting if it is off the edge left or right!!!!
			print("AHA")
			print(L_gridSpot)
			print(loopcount)
		loopcount = loopcount +1	
		
	#Uncomment to test
	
	#for L_gridSpot in L_gridList:
		#print(L_gridSpot)
			
		
			
	
	
	
	
	
															#Eventually 'null' will be replaced by the colour of the piece
validate_local_location(initialize_grid_string_start(), 'A1', 'null')	
#print(len(initialize_grid_string_start()))	
#print(validate_move_location('NNNNNNNNBBBBWWWWNNNNNNNNNNNBWNNNNNNWBNNNNNNNNNNNNNNNNNNNNNNNNNNN', 'H8'))


