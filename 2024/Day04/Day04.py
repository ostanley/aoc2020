from core.file_reader import yield_line
from core.geometry import Point2D

def p1_search(grid, starting_point):
    path = ["X","M","A","S"]
    total_xmases = 0
    for dir in starting_point.neighbours:
        curr_point = starting_point
        valid_path = 0
        while valid_path<3:
            curr_point += Point2D(*dir)
            valid_path+=1
            target = path[valid_path]
            
            if curr_point.pos() not in grid.keys() or grid[curr_point.pos()].value!=target:
                valid_path=-1
                break
            
        if valid_path>0:
            total_xmases += 1
    return total_xmases

def p2_search(grid, starting_point):
    diags = []
    for c in starting_point.neighbours:
        if 0 in c:
            continue
        test_point = starting_point + Point2D(*c)
        opposite_point = starting_point - Point2D(*c)
        if test_point.pos() in diags or test_point.pos() not in grid or opposite_point.pos() not in grid:
            continue
        if grid[test_point.pos()].value=="M" and grid[opposite_point.pos()].value=="S":
            diags += test_point.pos(), opposite_point.pos()
        elif grid[test_point.pos()].value=="S" and grid[opposite_point.pos()].value=="M":
            diags += test_point.pos(), opposite_point.pos()
    if len(diags)==4:
        return 1
    else:
        return 0

if __name__ == "__main__":
    file = "Day04/Day04input.txt"

    grid = {}
    for i, line in enumerate(yield_line(file)):
        for j, letter in enumerate(line):
            grid[(i,j)] = Point2D(i, j, letter, default_neighbours=True, diag=True)

    
    total_xmases = 0
    total_x_mases = 0

    for _, starting_point in grid.items():
        if starting_point.value == "X":
            total_xmases += p1_search(grid, starting_point)
        if starting_point.value=="A":
            total_x_mases += p2_search(grid, starting_point)
        
    print("Part 1: ", total_xmases)  
    print("Part 2: ", total_x_mases)