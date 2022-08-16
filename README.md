# Cup-Ball-Game
Attempt to mimic the behavior of a cup and ball game where the user has to guess the position of the ball once. 

The cup-ball game is a 2D representation of how a cup and ball game could behave. The position of the ball is randomized and the user has to guess both the row and column of where the ball could be positioned. The table is a 4 by 4 grid, but the user only needs to focus on the bottom table represented by 

'[['#', '#', '#', '#'], ['#', '#', '#', '#'], ['#', '#', '#', '#']] '. 

The user gains added difficulty if they are required to guess the row and column number of the ball, but the user can alter the code and remove the '#' placed behind 'print(row,col)'. Every time the user gets the incorrect answer, the correct answer will be displayed and the position of the ball is again randomized. The counter will increase by one until the correct answer is guessed. If the user is successful, it will congratulate the user in addition to stating the number of tries it took.
