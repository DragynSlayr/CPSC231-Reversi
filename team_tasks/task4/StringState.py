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
	L_y = L_xy[1]
	#########
	#|1|2|3|#
	#|4|x|5|#
	#|6|7|8|#	
	#########
	
	L_gridSpot1 = 'UA'
	L_gridSpot2 = 'UA'	
	L_gridSpot3 = 'UA'
	L_gridSpot4 = 'UA'
	L_gridSpot5 = 'UA'
	L_gridSpot6 = 'UA'
	L_gridSpot7 = 'UA'
	L_gridSpot8 = 'UA'
	LocalGridString = L_gridSpot1+ L_gridSpot2 +L_gridSpot3+ L_gridSpot4 +L_gridSpot5+ L_gridSpot6 +L_gridSpot7+ L_gridSpot8 
	
	#Top left corner
	if L_y ==1 and L_x == 0:
		#Only locations can be B1, A2, or B2
		L_gridSpot1 = 'U'
		L_gridSpot2 = 'U'
		L_gridSpot3 = 'U'
		L_gridSpot4 = 'U'
		L_gridSpot5 = 'B1'
		L_gridSpot6 = 'U'
		L_gridSpot7 = 'A2'
		L_gridSpot8 = 'B2'
		LocalGridString = L_gridSpot1+ L_gridSpot2 +L_gridSpot3+ L_gridSpot4 +L_gridSpot5+ L_gridSpot6 +L_gridSpot7+ L_gridSpot8 
		
	#Top right corner
	if L_y == 1 and L_x == 7:
		#Only locations can be G1, H1, or H2
		L_gridSpot1 = 'U'
		L_gridSpot2 = 'U'
		L_gridSpot3 = 'U'
		L_gridSpot4 = 'G1'
		L_gridSpot5 = 'U'
		L_gridSpot6 = 'G2'
		L_gridSpot7 = 'H2'
		L_gridSpot8 = 'U'
		LocalGridString = L_gridSpot1+ L_gridSpot2 +L_gridSpot3+ L_gridSpot4 +L_gridSpot5+ L_gridSpot6 +L_gridSpot7+ L_gridSpot8 
	
	#Bottom left corner
	if L_y == 8 and L_x == 0:
		#Only locations can be A7, B7, or B8
		L_gridSpot1 = 'U'
		L_gridSpot2 = 'A7'
		L_gridSpot3 = 'B7'
		L_gridSpot4 = 'U'
		L_gridSpot5 = 'B8'
		L_gridSpot6 = 'U'
		L_gridSpot7 = 'U'
		L_gridSpot8 = 'U'
		
		
	#Bottom right corner
	if L_y == 8 and L_x == 7:
		#Only locations can be G7, H7, or H8
		L_gridSpot1 = 'G7'
		L_gridSpot2 = 'H7'
		L_gridSpot3 = 'U'
		L_gridSpot4 = 'G8'
		L_gridSpot5 = 'U'
		L_gridSpot6 = 'U'
		L_gridSpot7 = 'U'
		L_gridSpot8 = 'U'
		LocalGridString = L_gridSpot1+ L_gridSpot2 +L_gridSpot3+ L_gridSpot4 +L_gridSpot5+ L_gridSpot6 +L_gridSpot7+ L_gridSpot8 
		
	#Top edge
	if L_y == 1:
		if L_x != 1 and L_x != 7:
			L_gridSpot1 = 'U'
			L_gridSpot2 = 'U'
			L_gridSpot3 = 'U'
			L_gridSpot4 = str(L_x -1)
			L_gridSpot5 = str(L_x+1)
			L_gridSpot6 =str( L_x +7)
			L_gridSpot7 = str(L_x +8)
			L_gridSpot8 = str(L_x +9)
			LocalGridString = L_gridSpot1+ L_gridSpot2 +L_gridSpot3+ L_gridSpot4 +L_gridSpot5+ L_gridSpot6 +L_gridSpot7+ L_gridSpot8 
			
	#Bottom edge
	if L_y ==8:
		if L_x != 1 and L_x != 7:
			L_gridSpot1 = str(L_x -9)
			L_gridSpot2 = str(L_x -8)
			L_gridSpot3 = str(L_x -7)
			L_gridSpot4 = str(L_x -1)
			L_gridSpot5 = str(L_x+1)
			L_gridSpot6 = 'U'
			L_gridSpot7 = 'U'
			L_gridSpot8 = 'U'
			LocalGridString = L_gridSpot1+ L_gridSpot2 +L_gridSpot3+ L_gridSpot4 +L_gridSpot5+ L_gridSpot6 +L_gridSpot7+ L_gridSpot8 
			
	#Left edge
	if L_x == 0:
		if L_y != 1 and L_y != 8:
			L_gridSpot1 = 'U'
			L_gridSpot2 = str(L_x -8)
			L_gridSpot3 = str(L_x -7)
			L_gridSpot4 = 'U'
			L_gridSpot5 = str(L_x+1)
			L_gridSpot6 = 'U'
			L_gridSpot7 = str(L_x+8)
			L_gridSpot8 = str(L_x+9)
			LocalGridString = L_gridSpot1+ L_gridSpot2 +L_gridSpot3+ L_gridSpot4 +L_gridSpot5+ L_gridSpot6 +L_gridSpot7+ L_gridSpot8 
	
	#Right edge
	if L_x ==7:
		if L_y != 1 and L_y != 8:
			L_gridSpot1 = str(L_x -9)
			L_gridSpot2 = str(L_x -8)
			L_gridSpot3 = 'U'
			L_gridSpot4 = str(L_x -1)
			L_gridSpot5 = 'U'
			L_gridSpot6 = str(L_x +7)
			L_gridSpot7 = str(L_x+8)
			L_gridSpot8 = 'U'
			LocalGridString = L_gridSpot1+ L_gridSpot2 +L_gridSpot3+ L_gridSpot4 +L_gridSpot5+ L_gridSpot6 +L_gridSpot7+ L_gridSpot8 
			
	#Any normal spot
	#for letter in LocalGridString:
	#	if letter == 'U' or 
	
	
#print(len(initialize_grid_string_start()))	
print(validate_move_location('NNNNNNNNBBBBWWWWNNNNNNNNNNNBWNNNNNNWBNNNNNNNNNNNNNNNNNNNNNNNNNNN', 'H8'))


