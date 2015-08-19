import math
import copy
import time

class Spot:
	'''
	The Spot class holds information about every position on the board
	It holds the x,y position, value, board size and domain.
	It also deletes a value from the domain if updated.
	'''
	def __init__(self,row,column,value,board_size):
		self.size = board_size*board_size
		self.row = row
		self.column = column
		self.value = value
		self.domain = range(self.size+1)[1:self.size+1]
		if value > 0:
			self.domain.remove(value)
			
	def addValue(self, value_to_add):
		self.value = value_to_add
		if self.value > 0:
			self.domain.remove(self.value)
	
class Board:
	'''
	The board class holds the size of the board and double array
	of spot objects in each position on the board.
	'''
	def __init__(self, size):
		self.size = size
		self.board = [[0 for x in xrange(size*size)] for x in xrange(size*size)]
		for x in range(size*size):
			for y in range(size*size):
				spot = Spot(x,y,0,size)
				self.board[x][y] = spot
	'''			
	This function creates the test boards to solve.	
	'''		
	def makeTestBoard(self, test_num):
		if (test_num == 1):
			self.board[0][0].addValue(2)
			self.board[0][1].addValue(1)
			self.board[1][1].addValue(3)
			self.board[1][2].addValue(2)
			self.board[2][3].addValue(4)
			self.board[3][0].addValue(1)
		if (test_num == 2):
			self.board[0][0].addValue(1)
			self.board[0][2].addValue(3)
			self.board[0][3].addValue(4)
			self.board[1][1].addValue(3)
			self.board[2][0].addValue(2)
			self.board[3][3].addValue(1)
		if (test_num == 3):
			self.board[0][1].addValue(3)
			self.board[0][2].addValue(5)
			self.board[0][4].addValue(8)
			self.board[0][8].addValue(9)
			self.board[1][6].addValue(6)
			self.board[1][8].addValue(3)
			self.board[2][2].addValue(8)
			self.board[2][3].addValue(3)
			self.board[2][6].addValue(7)
			self.board[3][1].addValue(1)
			self.board[3][3].addValue(4)
			self.board[3][8].addValue(2)
			self.board[4][1].addValue(7)
			self.board[4][3].addValue(9)
			self.board[4][5].addValue(3)
			self.board[4][7].addValue(6)
			self.board[5][0].addValue(3)
			self.board[5][5].addValue(2)
			self.board[5][7].addValue(5)
			self.board[6][2].addValue(3)
			self.board[6][5].addValue(5)
			self.board[6][6].addValue(2)
			self.board[7][0].addValue(7)
			self.board[7][2].addValue(9)
			self.board[8][0].addValue(4)
			self.board[8][4].addValue(7)
			self.board[8][6].addValue(8)
			self.board[8][7].addValue(3)
			self.board[8][8].addValue(6)
		if (test_num == 4):
			self.board[0][1].addValue(7)
			self.board[0][2].addValue(8)
			self.board[0][3].addValue(1)
			self.board[0][7].addValue(2)
			self.board[1][0].addValue(1)
			self.board[1][4].addValue(6)
			self.board[1][5].addValue(2)
			self.board[1][8].addValue(3)
			self.board[2][0].addValue(5)
			self.board[2][4].addValue(9)
			self.board[3][0].addValue(8)
			self.board[3][6].addValue(4)
			self.board[3][8].addValue(6)
			self.board[4][1].addValue(6)
			self.board[4][2].addValue(1)
			self.board[4][4].addValue(7)
			self.board[4][7].addValue(9)
			self.board[5][1].addValue(9)
			self.board[5][6].addValue(3)
			self.board[6][3].addValue(5)
			self.board[6][5].addValue(4)
			self.board[6][6].addValue(2)
			self.board[6][8].addValue(7)
			self.board[7][0].addValue(6)
			self.board[7][4].addValue(8)
			self.board[7][7].addValue(3)
			self.board[8][1].addValue(5)
			self.board[8][3].addValue(7)
			self.board[8][6].addValue(9)

	
	'''					
	This function prints the graphical representation of the 
	sudoku board.
	'''
	def printBoard(self):
		for x in range(self.size*self.size):
			for y in range(self.size*self.size):
				print '{:4}'.format(self.board[x][y].value),
			print
	
	'''
	getSpot returns the spot object at a certain position on the board.
	'''
	def getSpot(self, x, y):
		return self.board[x][y]


'''
Simple function to test if the board has been solved
Returns True if solve else False
'''
def isBoardSolved(board):
	size = board.size*board.size
	for x in range(size):
		for y in range(size):
			if (board.getSpot(x,y).value == 0):
				return False
	return True

'''
This function removes values from a domain at a specific spot in the board.
If the domain is reduced to one it places that value in the spot.
It returns and array of all the spots which may be affected if
the spots domain is reduced to 1.
'''
def checkDomainConstraints(spot, board):
	arc_consistancy = []
	if (spot.value == 0):
		for x in range(board.size*board.size):
			arc_consistancy.append(board.getSpot(x,spot.column))
			if board.getSpot(x,spot.column).value in spot.domain:
				spot.domain.remove(board.getSpot(x,spot.column).value)

		for x in range(board.size*board.size):
			arc_consistancy.append(board.getSpot(spot.row,x))
			if board.getSpot(spot.row,x).value in spot.domain:
				spot.domain.remove(board.getSpot(spot.row,x).value)

		a=int(math.ceil(spot.row/board.size))*board.size
		b=int(math.ceil(spot.column/board.size))*board.size
		for x in range(board.size):
			for y in range(board.size):
				arc_consistancy.append(board.getSpot(a+x,b+y))
				if board.getSpot(a+x,b+y).value in spot.domain:
					spot.domain.remove(board.getSpot(a+x,b+y).value)

		if (len(spot.domain)==1):
			spot.value = spot.domain[0]
			return arc_consistancy

	return arc_consistancy

'''		
This function takes in a board object and applies AC3 algorithm to it.
'''
def AC3(board):
	size = board.size
	for x in range(size*size):
		for y in range(size*size):
			arc_consistancy = []
			spot = board.getSpot(x,y)
			arc_consistancy = checkDomainConstraints(spot, board)
			if (len(arc_consistancy)>0):
				for i in range(len(arc_consistancy)):
					spot = arc_consistancy[i]
					checkDomainConstraints(spot, board)

'''
This function will use a recursive depth first search to replace the value of this spot with
each value of a domain that hasn't been reduced to one to see if one of the values lead to 
the solution.	
'''				
def backtracking(board):
	size = board.size*board.size
	for x in range(size):
		for y in range(size):
			if (board.getSpot(x,y).value == 0):
				for value in board.getSpot(x,y).domain:
					newBoard = copy.deepcopy(board)
					newBoard.getSpot(x,y).addValue(value)
					AC3(newBoard)
					if (isBoardSolved(newBoard)):
						newBoard.printBoard()
						return True
					backtracking(newBoard)

'''
If the puzzle is immediately solved by AC3 return the result
otherwise apply the recursive backtracking search for the result	
'''	
def backtrackingAC3(board):
	AC3(board)
	if (isBoardSolved(board)):
		board.printBoard()
		return True
	else:
		backtracking(board)
		

def main():
	t0 = 0
	finalTime = 0
	try:
		test_num = int(raw_input("Enter 1 or 2 to test 4x4 board\nEnter 3 or 4 to test 9x9 board: "))
	except ValueError:
		print "You must choose a valid number."
		exit()
	if (test_num == 1 or test_num == 2):
		board = Board(2)
		if (test_num == 1):
			board.makeTestBoard(1)
			print "Starting Board...."
			board.printBoard()
		if (test_num == 2):
			board.makeTestBoard(2)
			print "Starting Board...."
			board.printBoard()
		print "-----------------------------------"
		print "Solution Board ..."
		t0 = time.time()
		backtrackingAC3(board)
		finalTime = time.time() - t0
		print "\nTotal Time Algorithm Ran: "+str(finalTime)+" Seconds"
	elif (test_num == 3 or test_num == 4):
		board = Board(3)
		if (test_num == 3):
			board.makeTestBoard(3)
			print "Starting Board...."
			board.printBoard()
		if (test_num == 4):
			board.makeTestBoard(4)
			print "Starting Board...."
			board.printBoard()
		print "--------------------------------------------------------------"
		print "Solution Board ..."
		t0 = time.time()
		backtrackingAC3(board)
		finalTime = time.time() - t0
		print "\nTotal Time Algorithm Ran: "+str(finalTime)+" Seconds"
	else:
		print "You must choose a valid number."

main()

