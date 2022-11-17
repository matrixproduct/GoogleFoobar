# The problem is similar to the level 2 problem about knight's moves.
# The additional ingredient here is that we need also to iterate over all
# "virtual" maps with one wall removed. Two strategies are possible:
#  we can either find the shortest path for each virtual map and then find the minimum among them
#  or we can move on all virtual maps simultaneously until we reach the destination on one of them.
#  The second approach is faster, but the first one requires less memory and easier to implement,
#  so we choose the first one.


def neighbours(map, x, y):
    ''' Returns a list of all possible cells, which can be reached from a given
    cell (x,y) in one move'''
    h, w = len(map), len(map[0])  # height, width
    move = [1, -1]
    result = []
    for (new_x, new_y) in {(x + 1, y), (x - 1, y), (x,  y + 1), (x, y - 1)}:
        if 0 <= new_x < w and 0 <= new_y < h and not map[new_y][new_x]:
            result.append((new_x, new_y))
    return result


def shortest_path(map):
    ''' Returns the length of the shortest path for a given map, if the paths exists,
     otherwise returns 1000, which is greater than the length of any path'''
    h, w = len(map), len(map[0])  # height, width
    num_moves = 1
    visited = {(0, 0)}  # all cells visited before
    reached = {(0, 0)}  # all cells that can be reached after a given number of moves
    while True:  # we know that either the destination will be reached or there will be no new not visited cells
        num_moves += 1
        new_reached = set()  # reached after a new move
        for cell in reached:
            for new_cell in neighbours(map, *cell):
                if new_cell == (w - 1, h - 1):  # the destination is reached
                    return num_moves
                if new_cell not in visited:
                    visited.add(new_cell)
                    new_reached.add(new_cell)
        if new_reached == set():  # no new not visited cells
            return 1000
        reached = new_reached


def virtual_maps(map):
    '''Generates all possible virtual maps by removing "1" from all possible cells
    for a given map '''
    h, w = len(map), len(map[0])  # height, width
    yield map  # return the original map
    for y in range(h):
        for x in range(w):
            if map[y][x]:  # there is a wall
                v_map = [[elem for elem in row] for row in map]  # copy the map
                v_map[y][x] = 0  # remove the wall
                yield v_map


def solution(map):
    ''' Iterates over all virtual maps and finds the shortest path'''
    h, w = len(map), len(map[0])  # height, width
    path_len = []  # length of the shortest path for each virtual map
    for v_map in virtual_maps(map):
        path_len.append(shortest_path(v_map))
    return min(path_len)


