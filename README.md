# "The Mesh"
[Go to the game's website.](http://themeshgame.com/)

You are given some numbered tiles and a goal number tile. Your goal is to combine(add) the numbered tiles to reach the goal number. The tiles have 2 colors and different colored tiles have opposite signs. Double tapping a tile will change its color. The goal number does not have a sign, so the answer can have either sign.

If you use all the given numbered tiles to achieve the goal number, you move on to the next level. If you use all the given numbered tiles to achieve 0, the level restarts and no penalty is given.

If there are any numbered tiles left and no operations can be done to achieve the goal number, the level will restart, and you will lose however many tiles that were left behind. This limits the space you have to move the tiles around. If you run out of tiles, the game ends.

## Special Tiles
Combining a "x2" tile with a numbered tile will multiply the number by 2. The x2 tile will then disappear. Double tapping the x2 tile will change it to a ÷2 tile, which divides a number by 2.

Combining a "?" tile with a numberd tile will change the numbered tile to a different number. The ? tile will then disappear.

# MeshSolver
Solver to the mobile game "The Mesh."

User enters the given list of numbers and the goal number. The solver first finds all the possible operations to perform on the numbers. Then, the solver checks to see if any of the possible operations will result in the goal number. If no solution is found, the solver tries again, but sets the goal number to be 0. If no solution is found, the solver asks the user if they have a x2 that they can use. If so, the solver multiplies each number by 2, and tries to find a solution. If no solution is found, the solver asks if a ? tile exists. If so, the solver will ask the user to change a number with the ? tile, and then enter the new list of numbers
