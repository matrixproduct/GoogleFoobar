# ASSESSORS: PLEASE LOOK AT THE COMMENTS BELOW MY CODE, IF YOU WANT TO IMPROVE YOUR TESTS
#
# The main idea: we explore all possible paths recursively checking the set of all saved bunnies
# every time we arrive at the door, i. e. the last site. To optimise the process and to avoid infinite cycles
# we need to check two conditions:
#
# 1. Does it make sense to visit a new site? To this end we keep the information about all visited sites and
# the sets of the save bunnies and the corresponding times when we were at a given site. A new site should be visited if
# i) it hasn't been visited before or ii) new bunnies have been saved along the path or iii) the time is improved
#
# 2. The last condition of time improvement and fact that times can be negative may lead to appearance of an infinite
# path. To avoid such a path we can check from the very beginning the existence of cycles with negative total times.
# To find such cycles, it is enough to check only cycles with non-repeated elements (as any negative time cycle with
# repeated elements must contain at least one negative time cycle with non-repeated elements).

import copy
from itertools import permutations

current_path = [0]  # sites of the current path
best_saved = []  # the best set of saved bunnies for different paths; final output
visited = {}  # already visited sites with the corresponding values of saved sets and times


def worth_to_visit(T, saved, site):
    ''' Checks if it makes sense to visit a site and update the information about
    visited sites'''
    global best_saved
    if site not in visited:  # site hasn't been visited before
        visited[site] = [[saved, T]]
        return True
    lst = copy.copy(visited[site])
    updated = False
    for i, elem in enumerate(lst):
        if saved.issubset(elem[0]) and T <= elem[1]:  # new saved set is a subset of the existing one and new time <= T
            return False
        if saved == elem[0]: # new set = existing one, but the time is improved
            visited[site][i][1] = T
            updated = True
    if not updated:  # site has been visited before, but new bunnies are saved
        visited[site].append([saved, T])
    return True


def rec_sol(times, T, position):
    ''' Explores all possible paths recursively starting from position at time T'''
    global current_path, best_saved, visited
    n = len(times) - 2  # total number of bunnies
    saved = set(ind - 1 for ind in current_path if ind in range(1, n + 1))  # set of saved bunnies along the path

    for i in range(n + 2):  # check all sites
        delta = times[position][i]
        if i != position:  # except the current one
            new_T = T - delta
            new_saved = saved.union({i - 1}) if i in range(1, n + 1) else saved
            if worth_to_visit(new_T, new_saved, i):  # it makes sense to visit this site
                current_path.append(i)  # add new site to the path
                rec_sol(times, new_T, i)  # explore this possibility
                current_path.pop()  # return to the original path
    if position == n + 1 and T >= 0:  # we can escape and new save set is better
        if len(saved) > len(best_saved) or (len(saved) == len(best_saved) and sorted(list(saved)) < best_saved):
            best_saved = sorted(list(saved))


def negative_cycles(times):
    ''' Checks for negative cycles by calculating the toal time for all possible cycles
    with non-repeated elements'''
    sites_number = len(times)
    for l in range(2, sites_number + 1):  # l + 1 length of a cycle
        for path in permutations(range(sites_number), l):  # all possible permutations of length l
            if sum(times[path[i]][path[i + 1]] for i in range(l - 1)) + times[path[-1]][path[0]] < 0:
                return True
    return False


def solution(times, time_limit):
    global visited
    if negative_cycles(times):  # all bunnies can be saved
        return range(len(times) - 2)
    visited[0]=[[set(), time_limit]]  # initialise already visited sites
    rec_sol(times, time_limit, 0)
    return best_saved

# COMMENTS FOR ASSESSORS: After solving this problem I have found solutions from other people online.
# All of them were using some standard algorithms from graph theory and were variants of
# the same approach. One example of such a code is given below.
# Although it looks very elegant and PASSES ALL YOUR TESTS, it is actually generally INCORRECT,
# which can be seen by comparing its output with the output pf my code many for many different random inputs.
# One example:
#   input: times, T = ([[0, 2, 1, 3, 1], [3, 0, 2, 2, 2], [1, 2, 0, 2, 2], [3, 1, 2, 0, 1], [2, 1, 2, 3, 0]], 5)
#   output: [0, 2]
#   my output: [0, 1]
# You can convince yourself that my output is correct, as it can be obtained for the path: 0 -> 2 -> 1 -> 4
# I hope that this might help you to improve the tests.

# import itertools
#
# def solution_git(times, times_limit):
#     bunnies = len(times) - 2
#     shortest = floyd_warshall(times)
#     # negative cycle
#     for i in range(len(shortest)):
#         if shortest[i][i] < 0:
#             return range(bunnies)
#     for k in range(bunnies + 1, 1, -1):
#         for perm in itertools.permutations(range(1, bunnies + 1), k):
#             paths = edges(perm)
#             total_cost = 0
#             for x, y in paths:
#                 total_cost += shortest[x][y]
#             if total_cost <= times_limit:
#                 return sorted(list(i - 1 for i in perm))
#
#
# def edges(vertices):
#     nodes = [0] + list(vertices) + [-1]
#     paths = []
#     for i in range(len(nodes) - 1):
#         paths.append((nodes[i], nodes[i + 1]))
#
#     return paths
#
#
# def floyd_warshall(G):
#     nV = len(G)
#     distance = list(map(lambda i: list(map(lambda j: j, i)), G))
#
#     # Adding vertices individually
#     for k in range(nV):
#         for i in range(nV):
#             for j in range(nV):
#                 distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
#
#     return distance

