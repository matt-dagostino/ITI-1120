#------------------------------------------------
#            Assignment 3 - Labyrinth
#           Matteo Dagostino 300287930
#------------------------------------------------
import os
os.system('cls' if os.name == 'nt' else 'clear') # Clears the console

def to_list(string):
    list = []
    for char in string:
        list.append(char)
    return list

def starting_point(maze):
    for i in range(0, len(maze)):
        if A[i][0] == "p":
            return i,0

def ending_point(maze):
    for i in range(0, len(maze)):
        if A[i][15] == "p":
            return i,15

A = [to_list("################"),to_list("#ppppp#pps##pp##"), to_list("pp###pppp###pp##"), to_list("#p###pp#p##ppp##"), to_list("#pppp##pp##ppp##"),
to_list("####p###########"), to_list("###pp###########"), to_list("####ppppp#######"), to_list("########pp####pp"), to_list("########ppppppp#"), to_list("################") ]

starting = starting_point(A)
ending = ending_point(A)

#MAKE SURE 0's are as long as real labyrinth

temp_maze = []
for i in range(0,len(A)):
    l = []
    for j in range(0,16):
        l.append(0)
    temp_maze.append(l)
        
temp_maze[starting[0]][starting[1]] = 1

def next_move(move):
    for row in range(0, len(A)):
        for column in range(0, 16):
            if temp_maze[row][column] == move:
                #Going up
                if row > 0 and temp_maze[row-1][column] == 0 and A[row-1][column] == "p":
                    temp_maze[row-1][column] = move + 1
                #Going left
                if column > 0 and temp_maze[row][column-1] == 0 and A[row][column-1] == "p":
                    temp_maze[row][column-1] = move + 1
                #Going down
                if row < len(A)-1 and temp_maze[row+1][column] == 0 and A[row+1][column] == "p":
                    temp_maze[row+1][column] = move + 1
                #Going right
                if column < 16-1 and temp_maze[row][column+1] == 0 and A[row][column+1] == "p":
                    temp_maze[row][column+1] = move + 1


move = 0
while temp_maze[ending[0]][ending[1]] == 0:
    move = move + 1
    next_move(move)
length_path = move + 1
final_length = length_path

path = []
path.append((ending[0], ending[1]))
row = ending[0]
column = ending[1]

while length_path != 1:
    #Going down
    if row > 0 and temp_maze[row-1][column] == length_path-1:
        row = row-1
        path.append((row, column))
        length_path = length_path - 1
        A[row][column] = "v"
    #Going right
    elif column > 0 and temp_maze[row][column-1] == length_path-1:
        column = column-1
        path.append((row, column))
        length_path = length_path - 1
        A[row][column] = ">"
    #Going up
    elif row < len(A)-1 and temp_maze[row+1][column] == length_path-1:
        row = row + 1
        path.append((row, column))
        length_path = length_path -1
        A[row][column] = "^"
    #Going left
    elif column < 16-1 and temp_maze[row][column+1] == length_path-1:
        column = column + 1
        path.append((row, column))
        length_path = length_path -1
        A[row][column] = "<"

A[ending[0]][ending[1]] = ">"

print("------------------------ Output ------------------------")
print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in A]))
print("The length of the minimum path = " + str(final_length))
print()
print(path)