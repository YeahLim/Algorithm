# 지민이는 항구에서 일한다. 
# 그리고 화물을 배에 실어야 한다. 
# 모든 화물은 박스에 안에 넣어져 있다. 
# 항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다. 
# 모든 크레인은 동시에 움직인다.
# 각 크레인은 무게 제한이 있다. 
# 이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다. 
# 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. 
# N은 50보다 작거나 같은 자연수이다. 
# 둘째 줄에는 각 크레인의 무게 제한이 주어진다. 
# 이 값은 1,000,000보다 작거나 같다. 
# 셋째 줄에는 박스의 수 M이 주어진다. 
# M은 10,000보다 작거나 같은 자연수이다. 
# 넷째 줄에는 각 박스의 무게가 주어진다. 
# 이 값도 1,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 출력한다. 
# 만약 모든 박스를 배로 옮길 수 없으면 -1을 출력한다.


import sys
input = sys.stdin.readline
crane = int(input())
limited_weight = sorted(list(map(int, input().split())), reverse=True)
box = int(input())
boxes_weight = sorted(list(map(int, input().split())), reverse=True)

if limited_weight[0] < boxes_weight[0]: 
    print(-1)

else:
    answer = [0] * crane
    time = (box - 1) // crane + 1
    loaded_box = 0
    while loaded_box < box:
        print('==============')
        for i in range(crane):
            print('--------')
            if answer[i] < time and limited_weight[i] >= boxes_weight[loaded_box]:
                print('time:',time, 'answer[', i ,']:',answer[i])
                answer[i] += 1
                loaded_box += 1
                break
            if limited_weight[i] < boxes_weight[loaded_box]:
                print('두번째 if')
                time += 1
                break
    print(max(answer))


# import sys
# input = sys.stdin.readline
# crane = int(input())
# limited_weight = sorted(list(map(int, input().split())), reverse=True)
# box = int(input())
# boxes_weight = sorted(list(map(int, input().split())), reverse=True)
# if limited_weight[0] < boxes_weight[0]: 
#     print(-1)
# else:
#     answer = 0
#     while boxes_weight:
#         for limited in limited_weight:
#             if not boxes_weight:
#                 break
#             for i in range(len(boxes_weight)):
#                 if limited >= boxes_weight[i]:
#                     del boxes_weight[i]
#                     break
#         answer += 1
#     print(answer)