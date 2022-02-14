# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 여섯 가지이다.
    # push X: 정수 X를 큐에 넣는 연산이다.
    # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    # size: 큐에 들어있는 정수의 개수를 출력한다.
    # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 2,000,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 
# 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

from sys import stdin
input = stdin.readline
n = int(input())
queue = []
cnt = 0
for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if len(queue) != cnt:
            print(queue[cnt])
            cnt += 1
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue) - cnt)
    elif command[0] == 'empty':
        if len(queue) == cnt:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(queue) != cnt:
            print(queue[cnt])
        else:
            print(-1)
    else: # back
        if len(queue) != cnt:
            print(queue[-1])
        else:
            print(-1)

# def solve():
#     q = [0]*2000000
#     front = rear = 0
#     res = []
#     for string in sys.stdin.read().splitlines()[1:]:
#         t = string[1]
#         if t == "u":
#             q[rear] = string[5:]
#             rear += 1
#         elif t == "o":
#             if front == rear:
#                 res.append('-1')
#             else:
#                 res.append(q[front])
#                 front += 1
#         elif t == "i":
#             res.append(str(rear-front))
#         elif t == "m":
#             res.append('1' if front == rear else '0')
#         elif t == "r":
#             res.append(q[front] if front != rear else '-1')
#         elif t == "a":
#             res.append(q[rear-1] if front != rear else '-1')

#     sys.stdout.write('\n'.join(res))


# if __name__ == '__main__':
#     solve()