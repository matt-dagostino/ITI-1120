#------------------------------------------------
#            Assignment 3 - Labyrinth
#           Matteo Dagostino 300287930
#               mdago035@uottawa.ca
#------------------------------------------------
# This program will:
# ---> Find the minimum path to get to the end of the labyrinth (and display it)
# ---> Display the list of positions that Leon has to take to get the rocket launcher (s)
#------------------------------------------------
import os # Makes next line work
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

#Takes string input, turns string into a list, returns list
def to_list(string):
    list = []
    for char in string:
        list.append(char)
    return list

#Finds the starting point in the maze
def starting_point(maze):
    for i in range(0, len(maze)):
        if A[i][0] == "p":
            return i,0

#Finds where the rocket launcher is
def ending_point(maze):
    for i in range(0, len(maze)):
        for j in range(0, y):
            if A[i][j] == "s":
                return i,j

#Finds the ending point in the maze
def ending_point2(maze):
    for i in range(0, len(maze)):
        if A[i][y-1] == "p":
            return i,y-1

#Creates an empty maze with 1 as the starting point
def create_empty_maze(rows, columns):
    empty_maze = []
    for i in range(0,len(A)):
        l = []
        for j in range(0,y):
            l.append(0)
        empty_maze.append(l)
    empty_maze[rows][columns] = 1
    return empty_maze

#Adds a number next to the previous move (unless there is a wall) (print temp_maze to see a visual representation of this)
def next_move(move):
    for row in range(0, len(A)):
        for column in range(0, y):
            if temp_maze[row][column] == move:
                #Going up
                if row > 0 and temp_maze[row-1][column] == 0 and A[row-1][column] != "#":
                    temp_maze[row-1][column] = move + 1
                #Going left
                if column > 0 and temp_maze[row][column-1] == 0 and A[row][column-1] != "#":
                    temp_maze[row][column-1] = move + 1
                #Going down
                if row < len(A)-1 and temp_maze[row+1][column] == 0 and A[row+1][column] != "#":
                    temp_maze[row+1][column] = move + 1
                #Going right
                if column < y-1 and temp_maze[row][column+1] == 0 and A[row][column+1] != "#":
                    temp_maze[row][column+1] = move + 1

#Runs the next_move function as many times as needed
def make_move(ending0, ending1):
    move = 0
    while temp_maze[ending0][ending1] == 0:
        move = move + 1
        next_move(move)
    return move + 1

#Asks the user if they want to enter their own labyrinth or use a pre-made one (takes their input if they chose that option)
answer = str(input("Enter one of the following numbers: \n1) Enter my own labyrinth\n2) Use the preset labyrinth from the assignment\n---> "))
if answer == "1":
    A = []
    x = int(input("Enter the amount of rows that your labyrinth has: "))
    y = int(input("Enter the amount of columns that your labyrinth has: "))
    print("------------------------------------------------")
    print("When asked to input the rows, please enter them like this --> ############### or #ppp#pps#pp###")
    for i in range(0,x):
        A.append(to_list(str(input(str(i+1) + ") Enter a row: "))))
elif answer == "2":
    A = [to_list("################"),to_list("#ppppp#pps##pp##"), to_list("pp###pppp###pp##"), to_list("#p###pp#p##ppp##"), to_list("#pppp##pp##ppp##"),
    to_list("####p###########"), to_list("###pp###########"), to_list("####ppppp#######"), to_list("########pp####pp"), to_list("########ppppppp#"), to_list("################")]
    y = 16
else:
    print("Error: It seems like you have not entered 1 or 2. Please restart the program!")

#Set the starting and ending point
starting = starting_point(A)
ending = ending_point(A)

#Create the temporary maze, find how long the path will be
temp_maze = create_empty_maze(starting[0], starting[1])
length_path = make_move(ending[0], ending[1])

#Create path list, set the row and column to the end position
path = []
row = ending[0]
column = ending[1]

#Until the person has arrived to the starting point, do the following,
while length_path != 1:
    if row > 0 and temp_maze[row-1][column] == length_path-1:
        row = row-1
        path.append((row+1, column+1))
        length_path = length_path - 1
    elif row < len(A)-1 and temp_maze[row+1][column] == length_path-1:
        row = row + 1
        path.append((row+1, column+1))
        length_path = length_path -1
    elif column < y-1 and temp_maze[row][column+1] == length_path-1:
        column = column + 1
        path.append((row+1, column+1))
        length_path = length_path -1
    elif column > 0 and temp_maze[row][column-1] == length_path-1:
        column = column-1
        path.append((row+1, column+1))
        length_path = length_path - 1

#Set the starting and ending point
starting = ending_point(A)
ending = ending_point2(A)

#Create the temporary maze, find how long the path will be
temp_maze = create_empty_maze(starting[0], starting[1])
length_path = make_move(ending[0], ending[1])

#Create path list (2), set the row and column to the end position, add the end position to the path the person has to take
row = ending[0]
column = ending[1]
path2 = []
path2.append((row+1,column+1))

#Until the person has arrived to the starting point, do the following,
while length_path != 1:
    if column < y-1 and temp_maze[row][column+1] == length_path-1:
        column = column + 1
        path2.append((row+1, column+1))
        length_path = length_path -1
    elif row > 0 and temp_maze[row-1][column] == length_path-1:
        row = row-1
        path2.append((row+1, column+1))
        length_path = length_path - 1
    elif row < len(A)-1 and temp_maze[row+1][column] == length_path-1:
        row = row + 1
        path2.append((row+1, column+1))
        length_path = length_path -1
    elif column > 0 and temp_maze[row][column-1] == length_path-1:
        column = column-1
        path2.append((row+1, column+1))
        length_path = length_path - 1

#Reverse the paths (since right now they're from end -> start but we want the start -> end path)
path_reverse = path[::-1]
path2_reverse = path2[::-1]
path3 = []

#Add both paths (start -> rocket launcher, rocket launcher -> end) to one big path
for item in path_reverse:
    path3.append(item)
for item in path2_reverse:
    path3.append(item)

#Set the starting and ending point
starting = starting_point(A)
ending = ending_point2(A)

#Create the temporary maze, find how long the path will be, set row and column to end position
temp_maze = create_empty_maze(starting[0], starting[1])
length_path = make_move(ending[0], ending[1])
final_length = length_path
row = ending[0]
column = ending[1]

#Until the person has arrived to the starting point, do the following,
while length_path != 1:
    #Going down
    if row > 0 and temp_maze[row-1][column] == length_path-1:
        row = row-1
        length_path = length_path - 1
        A[row][column] = "v"
    #Going right
    elif column > 0 and temp_maze[row][column-1] == length_path-1:
        column = column-1
        length_path = length_path - 1
        A[row][column] = ">"
    #Going up
    elif row < len(A)-1 and temp_maze[row+1][column] == length_path-1:
        row = row + 1
        length_path = length_path -1
        A[row][column] = "^"
    #Going left
    elif column < y-1 and temp_maze[row][column+1] == length_path-1:
        column = column + 1
        length_path = length_path -1
        A[row][column] = "<"
A[ending[0]][ending[1]] = ">"

#Print final outputs below
print("------------------------ Output ------------------------")
print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in A]))
print("The length of the minimum path = " + str(final_length) + " (without getting rocket launcher)")
print("--------------------------------------------------------")
print("Below is the path that Leon needs to take in order to get the special rocket launcher:")
print(path3)
print()