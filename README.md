Solving Sudoku using AC3 and Backtracking
=========================================

Overview
--------

Each empty spot on the Sudoku board will have a domain of possible values that could be placed in the spot. AC3 will check each empty spot's row and column for existing values to eliminate from the domain. If the spot has one value left in its domain, it will fill the spot with that value. If AC3 is unable to reduce the domain to one then the backtracking method will be called. The backtracking method will randomly choose a value from the spot's domain, place it on the board, and apply AC3 again. The backtracking method will do this recursively until a solution is found and then return the solution.

Pre-requisites
--------------

   *Python 2.7

	
Running the app
---------------

   * Copy the BacktrackingAC3Sudoku folder or clone the repository
   * Run 'python BacktrackingAC3.py' from the BacktrackingAC3Sudoku directory
   * Follow instructions printed to terminal
	
Future Expansions
-----------------

   * Pull sudoku boards from a database instead of hardcoded test boards
   * Create a graphical user interface to select and display sudoku puzzles and solutions
