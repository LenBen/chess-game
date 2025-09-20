from pawn import Pawn

grid = [["",""],
        ["",""]]

for i in range(len(grid[0])):
    grid[0][i] = Pawn(i, 0, 1)

print(grid[0][1])
print(grid[0][0].can_move(grid, 1, 0))