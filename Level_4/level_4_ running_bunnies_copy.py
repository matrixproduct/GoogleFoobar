# n = total number of bunnies
# s = number of already saved bunnies
# l = number of bunnies not saved yet
# n = l + s
# T = time_limit
# saved = list of saved bunnies
# left = list of not saved bunnies
# position = current position
# visited = {site: [T, s]} already visited sites with the corresponding values of T and s
#
#
# is_enough_time(left)
# ''' Check whether it is enough time to save all left bunnies
#     iterating over all paths representing permutations (? not necessary to check all permutations)
#     of all sites with left bunnies
#     It prevents the algorithm to get in a trap of an unbounded increase of T'''
#
# rec_sol(times, T, saved, position, visited)
#     if position == bulkhead and T >= 0 and s == n
#         return  all
#
#     if is_enough_time
#         return all
#
#     for site in all sites except position:
#         check whether
#         i) it is reachable
#         ii) it is not visited or the situation is improved, i.e. s increases or T increases
#         then call re_sol with updated parameters get saved and append it to all_saved
#     if position == bulkhead and T >= 0
#         return best from all_saved
#     if no sites are reachable then
#         return []
import copy
from itertools import permutations
# can_save_all = False
current_path = [0]
best_saved = []  # the best set of saved bunnies for different paths
visited = {}  # already visited sites with the corresponding values of saved sets and T

# def is_enough_time(times, n, T, saved, position):
#     ''' Checks whether it is enough time to save all the left bunnies choosing a simplest path.
#      It prevents the algorithm to get in a trap of an unbounded increase of T'''
#     indx_left = [bun + 1 for bun in list(set([i for i in range(n)]) - saved)]
#     left = [position] + indx_left + [n+1]
#     t = sum(times[left[i]][left[i + 1]] for i in range(len(left) - 1))
#     return T >= t


def worth_to_visit(T, saved, site):
    global can_save_all, best_saved
    path = current_path + [site]
    if site not in visited:
        visited[site] = [[saved, T, path]]
        return True
    lst = copy.copy(visited[site])
    updated = False
    for i, elem in enumerate(lst):
        if saved.issubset(elem[0]) and T <= elem[1]:
            return False
        if saved == elem[0]:
            # can_save_all = True
            #best_saved = range(n)
            # return True
            visited[site][i][1] = T
            visited[site][i][2] = path
            updated = True
    if not updated:
        visited[site].append([saved, T, path])
    return True


def rec_sol(times, T, position):
    global current_path, best_saved, visited
    # if can_save_all:
    #     return
    n = len(times) - 2  # total number of bunnies
    saved = set(ind - 1 for ind in current_path if ind in range(1, n + 1))
    # s = len(saved)  # number of saved already bunnies
    # print(position)

    # if (position == n + 1 and T >= 0 and s == n) or is_enough_time(times, n, T, saved, position):
    #     best_saved = range(n)  # all bunnies can be saved
    #     can_save_all = True
    #     return

    for i in range(n + 2):
        delta = times[position][i]
        if i != position:  # check all sites except the current one
            new_T = T - delta
            new_saved = saved.union({i - 1}) if i in range(1, n + 1) else saved
            # if i not in visited or new_T > visited[i][0] or new_s > visited[i][1]:
            if worth_to_visit(new_T, new_saved, i):  # it makes sense to visit this site
                # if can_save_all:
                #     return
                new_sites_visited = True
                # c_saved = new_saved.copy()  # local copy of saved
                current_path.append(i)
                # c_visited = copy.deepcopy(visited)  # local copy of visited
                # c_visited[i] = [new_T, new_s]  # update visited sites
                rec_sol(times, new_T, i)
                # if can_save_all:
                #     return
                current_path.pop()
    if position == n + 1 and T >= 0:  # we can escape and new save set is better
        if len(saved) > len(best_saved) or (len(saved) == len(best_saved) and sorted(list(saved)) < best_saved):
            best_saved = sorted(list(saved))


def negative_cycles(times):
    sites_number = len(times)
    for l in range(2, sites_number + 1):
        for path in permutations(range(sites_number), l):
            if sum(times[path[i]][path[i + 1]] for i in range(l - 1)) + times[path[-1]][path[0]] < 0:
                return True
    return False

def solution(times, time_limit):
    global visited
    n = len(times) - 2  # total number of bunnies
    if negative_cycles(times):
        return range(n)
    visited[0]=[[set(), time_limit,[0]]]  # already visited sites with the corresponding values of saved sets and T
    rec_sol(times, time_limit, 0)
    return best_saved


print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
# Output:
#     [0, 1]
# print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))
# Output:
#     [1, 2]
#print(solution([[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]], 2))



# times = [[0, -1], [0, 0]]
# times = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
# times = [[0, 1, 1, 1, 1], [10, 0, -1, 10, 10], [10, 10, 0, 1, 10], [10, -1, 10, 0, 10], [1, 1, 1, 1, 0]]
# print(negative_cycles(times))

#T = 0
# times = [[0, 2, -2, 2, 1], [9, 0, 2, 2, -1], [9, 13, 0, 12, 11], [9, 3, 2, 0, -1], [9, -3, 2, 2, 0]]
# T = 2

#print(solution(times, T))

# print(solution([[0, 10, 10, -1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]], 2))

#sd =[[1], [0]]
#print(best(sd))
