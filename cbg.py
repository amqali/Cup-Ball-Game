import random

def cup_ball_game():

    guess_count = (0)

    # generates randomized table (cup & ball table)
    
    print('\n')
    for i in range(4):
        x = [['#']*4 for i in range(3)]
        x[random.randint(0,2)][random.randint(0,3)] = 'o' # 'o' is represented as the ball hidden underneath a cup.
        print(x)
    
    print("[['#', '#', '#', '#'], ['#', '#', '#', '#'], ['#', '#', '#', '#']] \n")


    while True:
        
        # counter will increase by 1 until the correct position of the ball is found
        
        guess_count += 1

        # position of the ball randomized for each round.
        
        row = random.randint(0,3)
        col = random.randint(0,2)

        # print(row,col) remove '#' if you want the answer. 

        guess1 = int(input("Row (0,1,2,3): "))
        guess2 = int(input("Col (0,1,2): "))
            
        # checks for the ball position by comparing it to user input.

        
        if guess1 != row and guess2 != col: 
            print("\nWrong, Correct Answer is: row: {r} , col: {c}".format(r=row, c=col))
            y = input("Try again? (y/n): ")
            if y == "y":
                table() == True
            else:
                break

        elif guess1 == row and guess2 == col: 
            print("Well done, correct answer after {g} tries".format(g=guess_count))
            break

# call the cup_ball_game function to initiate the game. 

cup_ball_game()
