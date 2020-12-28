Constraint satisfaction problems (CSP) - Map Coloring

A CSP is a problem composed of a finite set of variables each of which has a finite domain of values and a set of constraints. Each constraint is defined over some subset of the original set of variables and restricts the values these variables can simultaneously take. The task is to find an assignment of a value for each variable such that the assignments satisfy all the constraints In some problems the goal is to find all such assignments. Constraint satisfaction problems on finite domains are typically solved using a form of search. The most used techniques are variants of backtracking, constraint propagation, and local search.


Program Content:
DFS:
The concept of backtracking is applied to map coloring, once any variables domain reaches 0 then the algorithm backtracks and checks other options in the domain which would yield a color for the one with the empty set in its domain. Every time the algorithm checks the next state only after reaching there, there are no prechecks done.
DFS WITH FORWARD CHECKING: 
The concept here is exactly same as backtracking only that next check is pre-checked by adding and removing the state domain variables which making the algorithm smarter than DFS. Number of backtrackings are significantly reduced.
DFS WITH FORWARD CHECKING AND PROPAGATION THROUGH SINGLETON DOMAINS: 
Here the algorithm checks among all possibilities of next states and choses the one with domain value equal to 1 and propagates to the next unassigned variables from the one with domain 1.
HEURISTICS:
There may be several options or nodes to choose from the next states. Any one of the states may be chosen at random and we could progress the map coloring algorithm. With using heuristics, we get an order of choosing the variables depending on some factors. 
MINIMUM REMAINING VALUES:
In MRV heuristic propagation follows in the order of those nodes with least number of values in its domain. With respect to the problem If one state has 4 permissible values in its domain and another state has 2 then the state with 2 values would be chosen first, here permissible refers to reducing state domain because of constraints imposed that adjacent states cannot have same color
DEGREE HEURISTIC:
The idea here is assign a value to the variable that is involved in the largest number of constraints on other unassigned variables. It is often used as a means to reduce the number of same next possibilities, as a tie breaker with Minimum remaining values heuristic to choose the best next when all next nodes have the same number of domain values after a variable assignment is done using MRV.
LEAST CONSTRAINING VALUE:	
Here the chosen heuristic rules out the fewest values in the remaining variables.
