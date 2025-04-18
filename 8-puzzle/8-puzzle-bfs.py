import sys
from collections import deque

def solvable(initial_state):
    inversions = 0
    state = [x for x in initial_state if x != 0]
    for i in range(8):
        for j in range(i+1, 8):
            if state[i] > state[j]:
                inversions += 1
    return inversions % 2 == 0

def get_position(state):
    k = state.index(0)
    return k // 3, k % 3

def solution(initial_state, final_state):
    queue = deque()
    queue.append([initial_state, 0])
    visited = set()

    row_move = [1, 0, -1, 0]
    col_move = [0, -1, 0, 1]

    while queue:
        state, moves = queue.popleft()
        
        if state == final_state:
            print(moves)
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
                if tuple(new_state) not in visited:
                    visited.add(tuple(new_state))
                    queue.append([new_state, moves + 1])

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