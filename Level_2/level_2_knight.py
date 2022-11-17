def index_to_coord(ind):
    ''' Converts index of a cell, which is an integer from 0 to 63,
     to coordinates (x, y), where x and y are integers from 0 to 7'''
    x = ind % 8
    y = ind // 8
    return x, y


def neighbours(x, y):
    ''' Returns a list of all possible cells, which can be reached from a given
    cell (x,y) in one move'''
    short_jump, long_jump = [1, -1], [2, -2]
    result = []
    for s in short_jump:
        for l in long_jump:
            if 0 <= x + s <= 7 and 0 <= y + l <= 7:
                result.append((x + s, y + l))
            if 0 <= y + s <= 7 and 0 <= x + l <= 7:
                result.append((x + l, y + s))
    return result


def solution(src, dest):
    x0, y0 = index_to_coord(src)
    x1, y1 = index_to_coord(dest)
    if (x0, y0) == (x1, y1):
        return 0
    num_moves = 1
    visited = {(x0, y0)}  # all cells visited before
    reached = {(x0, y0)}  # all cells that can be reached after a given number of moves
    while True:  # we know that the destination will be always reached
        new_reached = set()  # reached after a new move
        for cell in reached:
            for new_cell in neighbours(*cell):
                if new_cell == (x1, y1):  # the destination is reached
                    return num_moves
                visited.add(new_cell)
                new_reached.add(new_cell)
        reached = new_reached
        num_moves += 1


print(solution(0,0))
