import copy

def is_enough_time(times, n, T, saved, position):
    ''' Checks whether it is enough time to save all the left bunnies choosing a simplest path.
     It prevents the algorithm to get in a trap of an unbounded increase of T'''
    indx_left = [bun + 1 for bun in list(set([i for i in range(n)]) - saved)]
    left = [position] + indx_left + [n+1]
    t = sum(times[left[i]][left[i + 1]] for i in range(len(left) - 1))
    return T >= t


def best():
    global all_saved
    '''Returns the best option from all possible lists of saved bunnies'''
    if not all_saved:
        return []
    bst = all_saved[0]
    for saved in all_saved:
        if len(saved) > len(bst) or (len(saved) == len(bst) and saved < bst):
            bst = saved
    return bst


def worth_to_visit(T, saved, site):
    global visited
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
    s = len(saved)  # number of saved already bunnies
    # print(position)

    if (position == n + 1 and T >= 0 and s == n) or is_enough_time(times, n, T, saved, position):
        all_saved.append([i for i in range(n)])  # all bunnies can be saved
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
    if position == n + 1 and T >= 0:  # we can escape
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
    # print(visited)
    return best()
