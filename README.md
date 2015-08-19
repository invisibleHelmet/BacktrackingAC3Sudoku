Solving Sudoku using AC3 and Backtracking
=========================================

Overview
--------

AC3 uses constraints to limit the possible values for each variable or remove values from the variables domain. If a domain is limited to one value from the constraints AC3 will then update all the affected variables domains to see if it can further reduce their domains. This process is a type of inference called constraint propagation. As you will see in my implementation, constraint propagation can not always completely limit the domain to one value. If multiple domains can not be limited to one value then it will not find a solution to the puzzle. To ensure a solution after using AC3 a method called backtracking can be used. Backtracking applies searching to constraint propagation to ensure a solution. When there are multiple values left in a domain of a variable backtracking will choose each one and apply constraint propagation again to see if it can find the correct values to remove from the domains.

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
