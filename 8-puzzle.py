class Node:
    def __init__(self, array, i, j, g, parent):
        self.array = array
        self.h = float('inf')
        self.i = i
        self.j = j
        self.g = g
        self.parent = parent

def h(initial, final):
    count = 0
    for i in range(3):
        for j in range(3):
            if initial[i][j] != 0 and initial[i][j] != final[i][j]:
                count += 1
    return count

def print_queue(queue, ptr, best_node):
    first = []
    second = []
    third = []
    g, h = best_node.g, best_node.h
    first.append(' '.join(map(str, best_node.array[0])) + f' g={g}')
    second.append(' '.join(map(str, best_node.array[1])) + f' h={h}')
    third.append(' '.join(map(str, best_node.array[2])) + f' f={g+h}')
    for node in queue[ptr:]:
        if node != best_node:
            g, h = node.g, node.h
            first.append(' '.join(map(str, node.array[0])) + f' g={g}')
            second.append(' '.join(map(str, node.array[1])) + f' h={h}')
            third.append(' '.join(map(str, node.array[2])) + f' f={g+h}')
    print('    '.join(map(str,first)))
    print('    '.join(map(str,second)))
    print('    '.join(map(str,third)))
    print('  ↓  ')

def solution(initial, i, j, final): 
    queue = []
    queue_ptr = 0
    root_node = Node(initial, i, j, 0, None)
    root_node.h = h(initial, final)
    queue.append(root_node)

    row_move = [1, 0, -1, 0]
    col_move = [0, -1, 0, 1]

    while queue:

        # 예측값이 가장 작은 노드 선택
        best_node = min(queue, key=lambda n: n.h + n.g)
        print_queue(queue, queue_ptr, best_node)
        queue_ptr = len(queue) - 1
        queue.remove(best_node)

        # 선택된 노드가 목표 상태인지 검사
        if best_node.h == 0:
            print('Goal!')
            return

        # 선택된 노드 확장
        for k in range(4):
            new_i = best_node.i + row_move[k]
            new_j = best_node.j + col_move[k]
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_array = []
                for row in best_node.array:
                    new_array.append(row.copy())
                tmp = new_array[new_i][new_j]
                new_array[new_i][new_j] = 0
                new_array[best_node.i][best_node.j] = tmp
                child = Node(new_array, new_i, new_j, best_node.g+1, best_node)
                child.h = h(child.array, final)
                queue.append(child)

if __name__ == '__main__':
    # 초기 상태
    initial = [
        [0, 1, 2],
        [4, 5, 3],
        [7, 8, 6]
    ]

    # 목표 상태
    final = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    # 빈 칸의 위치 지정
    i, j = 0, 0
    for i in range(3):
        for j in range(3):
            if initial[i][j] == 0:
                break
        else:
            continue
        break

    solution(initial, i, j, final)
