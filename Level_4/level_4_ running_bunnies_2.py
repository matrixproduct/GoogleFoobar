import copy, itertools

can_save_all = False
current_path = [0]
all_saved = []  # list of all saved bunnies for different paths
visited = {}  # already visited sites with the corresponding values of saved sets and T


def best(all_saved):
    '''Returns the best option from all possible lists of saved bunnies'''
    if not all_saved:
        return []
    bst = all_saved[0]
    for saved in all_saved:
        if len(saved) > len(bst) or (len(saved) == len(bst) and saved < bst):
            bst = saved
    return bst


def is_enough_time(times, n, T, saved, position):
    ''' Checks whether it is enough time to save all the left bunnies choosing a simplest path.
     It prevents the algorithm to get in a trap of an unbounded increase of T'''
    indx_left = [bun + 1 for bun in list(set([i for i in range(n)]) - saved)]
    left = [position] + indx_left + [n+1]
    t = sum(times[left[i]][left[i + 1]] for i in range(len(left) - 1))
    if T>=t:
        visited[len(times) - 1].append([set([i for i in range(n)]), T - t, current_path + indx_left[1:]])
    return T >= t


def worth_to_visit(T, saved, site):
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
            visited[site][i][1] = T
            visited[site][i][2] = path
            updated = True
    if not updated:
        visited[site].append([saved, T, path])
    return True


def rec_sol(times, T, position):
    global can_save_all, current_path, all_saved, visited

    if can_save_all:
        return
    n = len(times) - 2  # total number of bunnies
    saved = set(ind - 1 for ind in current_path if ind in range(1, n + 1))
    # s = len(saved)  # number of saved already bunnies
    # print(position)

    if (position == n + 1 and T >= 0 and len(saved) == n) or is_enough_time(times, n, T, saved, position):
        all_saved.append([i for i in range(n)])  # all bunnies can be saved
        print("can_save_all")
        can_save_all = True
        return

    new_sites_visited = False
    for i in range(n + 2):
        delta = times[position][i]
        if i != position:  # check all sites except the current one
            new_T = T - delta
            new_saved = saved.union({i - 1}) if i in range(1, n + 1) else saved
            # if i not in visited or new_T > visited[i][0] or new_s > visited[i][1]:
            if worth_to_visit(new_T, new_saved, i):  # it makes sense to visit this site
                new_sites_visited = True
                # c_saved = new_saved.copy()  # local copy of saved
                current_path.append(i)
                # c_visited = copy.deepcopy(visited)  # local copy of visited
                # c_visited[i] = [new_T, new_s]  # update visited sites
                rec_sol(times, new_T, i)
                current_path.pop()
    if position == n + 1 and T >= 0 and saved:  # we can escape
        all_saved.append(sorted(list(saved)))
        # print(saved, visited)
        return
    if not new_sites_visited:
        return


def solution(times, time_limit):
    global can_save_all, current_path, all_saved, visited
    # n = len(times) - 2  # total number of bunnies
    #T = time_limit  # time left
    # saved = set() # already saved bunnies
    #s = len(saved)
    #position = 0  # current site
    visited[0]=[[set(), time_limit,[0]]]  # already visited sites with the corresponding values of saved sets and T
    rec_sol(times, time_limit, 0)
    best_saved = best(all_saved)
    # for key, value in visited.items():
    for elem in visited[len(times) - 1]:
            if elem[0] == set(best_saved) and elem[1] >=0:
                print(elem[2])
    return best_saved


def direct(times, T, limit_length):
    m = len(times); n = m - 2
    all_direct_saved = []
    sites = set([i for i in range(m)])
    for l in range(1, limit_length + 1):
        for chain in itertools.product(sites, repeat=l):
            path = [0] + list(chain) + [m-1]
            t = sum(times[path[i]][path[i + 1]] for i in range(len(path) - 1))
            if t <= T:
                saved = set(ind - 1 for ind in path if ind in range(1, n + 1))
                all_direct_saved.append(sorted(list(saved)))

    return best(all_direct_saved)


# print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
# Output:
#     [0, 1]
# print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))
# Output:
#     [1, 2]
#
#times = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
# T = 3
times = [[0, 1], [0, 0]]
T = 0
# times = [[0, 2, -2, 2, 1], [9, 0, 2, 2, -1], [9, 13, 0, 12, 11], [9, 3, 2, 0, -1], [9, -3, 2, 2, 0]]
# T = 2
limit_length = 7
# print(solution(times, T))
# print('Direct: ', direct(times, T, limit_length))
print(solution([[0, 1, 1, 3, 1, 3, 1], [2, 0, 2, 3, 3, 1, 3], [3, 2, 0, 1, 3, 2, 2], [2, 3, 2, 0, 3, 1, 2],
                 [2, 2, 2, 1, 0, 2, 1], [1, 1, 1, 3, 1, 0, 3], [3, 1, 1, 1, 1, 2, 0]], 2))

# test = [[],[]]
# print(best(test))