import sys
import heapq

def solvable(initial_state):
    inversions = 0
    state = [x for x in initial_state if x != 0]
    for i in range(8):
        for j in range(i+1, 8):
            if state[i] > state[j]:
                inversions += 1
    return inversions % 2 == 0

def heuristic(state, final_state):
    h = 0
    for a in range(9):
        if state[a] == 0:
            continue
        for b in range(9):
            if state[a] == final_state[b]:
                row_diff = a // 3 - b // 3
                col_diff = a % 3 - b % 3
                h += abs(row_diff) + abs(col_diff)
    return h

def get_position(state):
    k = state.index(0)
    return k // 3, k % 3

def solution(initial_state, final_state):
    g = 0
    h = heuristic(initial_state, final_state)
    f = g + h
    queue = [(f, g, initial_state)]
    visited = set()

    row_move = [1, 0, -1, 0]
    col_move = [0, -1, 0, 1]

    while queue:
        f, g, state = heapq.heappop(queue)
        
        if state == final_state:
            print(g)
            return

        i, j = get_position(state)

        for k in range(4):
            new_i = i + row_move[k]
            new_j = j + col_move[k]
            if 0<=new_i<=2 and 0<=new_j<=2:
                new_state = state.copy()
                old_index = i * 3 + j
                new_index = new_i * 3 + new_j
                new_state[old_index], new_state[new_index] = new_state[new_index], new_state[old_index]
                new_state_tuple = tuple(new_state)
                if new_state_tuple not in visited:
                    new_g = g + 1
                    new_h = heuristic(new_state, final_state)
                    new_f = new_g + new_h
                    visited.add(new_state_tuple)
                    heapq.heappush(queue, (new_f, new_g, new_state))

final_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
initial_states = []

n = sys.stdin.readline().rstrip()
sys.stdin.readline().rstrip()

for _ in range(int(n)):
    state_input = []
    for _ in range(3):
        row = list(sys.stdin.readline().rstrip())
        if '#' in row:
            row[row.index('#')] = 0
        state_input.extend([int(x) for x in row])
    initial_states.append(state_input)
    sys.stdin.readline().rstrip()
    
for initial_state in initial_states:
    if solvable(initial_state):
        solution(initial_state, final_state)
    else:
        print('impossible')