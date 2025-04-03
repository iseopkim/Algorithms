import heapq

def heuristic(initial_state):
    final = [49, 50, 51, 52, 53, 54, 55, 56, 35]
    h = 0
    for i in range(9):
        if initial_state[i] != 35:
            for j in range(9):
                if initial_state[i] == final[j]:
                    h += abs(i // 3 - j // 3) + abs(i % 3 - j % 3)
                    break
    return h

#  0  1  2  3  4  5  6  7  8  9  10 11 12 13
# [1, 2, 3, 4, 5, 6, 7, 8, #, i, j, g, h, f]

def solution(initial_state):
    root_node = initial_state
    root_node[12] = heuristic(root_node)
    root_node[13] = root_node[12]
    root_node_key = tuple(root_node[0:9])
    open = dict()
    closed = dict()
    open[root_node_key] = root_node
    heap_open = [(open[root_node_key][13], root_node_key)]
    heapq.heapify(heap_open)
    row_move = [1, 0, -1, 0]
    col_move = [0, -1, 0, 1]
    while open:
        flag = True
        while flag:
            min_f, best_node_key = heapq.heappop(heap_open)
            if open[best_node_key]:
                best_node = open[best_node_key]
                flag = False
        if best_node[12] == 0:
            print(best_node[11])
            return
        del open[best_node_key]
        closed[best_node_key] = best_node
        for k in range(4):
            new_i = best_node[9] + row_move[k]
            new_j = best_node[10] + col_move[k]
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                old_point = 3 * best_node[9] + best_node[10]
                new_point = 3 * new_i + new_j
                child_node = best_node.copy()
                tmp = child_node[new_point]
                child_node[new_point] = 35
                child_node[old_point] = tmp
                child_node_key = tuple(child_node[0:9])
                child_node[9] = new_i
                child_node[10] = new_j
                child_node[11] = best_node[11] + 1   # g
                child_node[12] = heuristic(child_node)    # h
                child_node[13] = child_node[11] + child_node[12]   # f
                if child_node_key in open:
                    if open[child_node_key][13] <= child_node[13]:
                        continue
                elif child_node_key in closed:
                    continue
                else:
                    open[child_node_key] = child_node
                    heapq.heappush(heap_open, (child_node[13], child_node_key))

def solvable(initial_state):
    inversions = 0
    array = initial_state[:9]
    for i in range(9):
        if array[i] == 35:
            continue
        for j in range(i+1, 9):
            if array[j] == 35:
                continue
            elif array[i] > array[j]:
                inversions += 1
    return inversions % 2 == 0

if __name__ == '__main__':
    iteration = int(input())
    input()
    initial_states = []
    meta_info = [0, 0, 0, float('inf'), float('inf')]   # i, j, g, h, f
    for _ in range(iteration):
        input_1 = input()
        line_1 = [ord(x) for x in input_1]
        input_2 = input()
        line_2 = [ord(x) for x in input_2]
        input_3 = input()
        line_3 = [ord(x) for x in input_3]
        initial_states.append(line_1 + line_2 + line_3 + meta_info)
        input()
    for initial_state in initial_states:
        n = 0
        for i in range(9):
            if initial_state[i] == 35:
                n = i
                break
            else:
                continue
        i = n // 3
        j = n % 3
        initial_state[9] = i
        initial_state[10] = j
        if solvable(initial_state):
            solution(initial_state)
        else:
            print('impossible')