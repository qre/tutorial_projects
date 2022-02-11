import random
import re

#creating a board(object) to represent the game
#this is so that we can just say "create a board object" or
#"dig here" or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        #lets keep track of these parameters
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #lets create a board (helper function)
        self.board = self.make_new_board() #the bombs have been planted!
        self.assign_values_to_board()

        #initialize a set to keep track of which locations we've uncovered
        #well save the tuples (row,col) into this set
        self.dug = set() #in case player digs at 0, 0 -> self.dug={(0, 0)}

    def make_new_board(self):
        #make a new board with dim_size and num_bombs
        #then we make a list of lists (optimal for a 2d board)

        #generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        #planting the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2-1) #randomint N a<=N<=b
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*': # *=bomb
            #we planted the bomb, moving on. Only works with a while loop
                continue
        
            board[row][col] = '*'
            bombs_planted += 1
        return board
    def assign_values_to_board(self):
        #after planting the bombs we'll assign a number 0-8 for all the empty spaces, which
        #illustrates how many neighbouring bombs there are. We can precompute these and itll save us
        #some effort checking whats arounf the board later on
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighbouring_bombs(r,c)
    def get_num_neighbouring_bombs(self, row, col):
        #now we iterate through each of the neighbouring positions and sum number of bombs
        #top left: (row-1, col-1)
        #top mid: (row-1, col)
        #top right: (row-1, col+1)
        #left: (row, col-1)
        #mid: (row, col)
        #right: (row, col+1)
        #bot left: (row+1, col-1)
        #bot mid: (row+1, col)
        #bot right: (row+1, col+1)

        #make sure not to go OOB!

        num_neighbouring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    #our original location, dont check (???Like, do we always start in the middle?)
                    continue
                if self.board[r][c] == '*':
                    num_neighbouring_bombs += 1

        return num_neighbouring_bombs

    def dig(self, row, col):
        #dig at specified location
        #True if successful dig, False if a bomb

        #some scenarios:
        #hit bomb=game over
        #dig at a spot with neighbouring bombs-> dig finished
        #dig at a spot with no neighbouring bombs-> dig neighbouring spots recursively

        self.dug.add((row, col)) #keeping track of spots already dug

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        #self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if(r, c) in self.dug:
                    continue #means this spot has already been dug
                self.dig(r, c)

        #if our 1st dig didnt hit a boms we shouldnt hit a bomb here
        return True

    def __str__(self):
        #special function. If you print this out
        #itll print out what this function returns (o.O)
        #return a string that shows the board to the player


        #lets create an array that represents what the user will see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        #put this together in a string
        return '|'.join(str(visible_board)) #like this i guess?

def play(dim_size=10, num_bombs=10):
    # 1:create the board and plant the bombs
    board = Board(dim_size, num_bombs)
    # 2:show the board to the user and ask where they want to dig
    # 3a: if location=bomb, game over!
    # 3b: in case location is not a bomb, dig recursively until each square is at least next to a bomb
    # 4:repeat steps 2 and 3a/b until theres nowhere to dig
    safe = True
    
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        #re splits input, so user can type smth like this: 4,1 or 7, 9 or 3,   6
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: ")) # 4, 7
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row>= board.dim_size or col <0 or col>= board.dim_size:
            print("OOB! Try again")
            continue

        #if input is valid, we dig
        safe = board.dig(row,col)
        if not safe:
            #means weve hit a bomb
            break # gameover
    #2 ways to end the loop here
    if safe:
        print("CONGRATS!! YOU WON!")
    else:
        print("U SUCK, GAME OVER!")
        #in case user lost, we can reveal the board
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__': #not necessary, but good practice
    play()
