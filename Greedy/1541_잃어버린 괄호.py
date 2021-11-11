# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 
# 그리고 나서 세준이는 괄호를 모두 지웠다.
# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 
# 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 
# 수는 0으로 시작할 수 있다. 
# 3입력으로 주어지는 식의 길이는 50보다 작거나 같다.

# 출력
# 첫째 줄에 정답을 출력한다.

import sys
exp = sys.stdin.readline().strip().split('-')

answer = 0
for x in exp[0].split('+'):
    answer += int(x)
# answer = sum(map(int, exp[0].split('+')))

for x in exp[1:]:
    for y in x.split('+'):
        answer -= int(y)
print(answer)

# import sys
# exp = sys.stdin.readline().strip().split('-')
# if '+' in exp[0]:
#     answer = sum(map(int, exp.pop(0).split('+')))
# else:
#     answer = int(exp.pop(0))
# for x in exp:
#     if '+' in x:
#         num = map(int, x.split('+'))
#         answer -= sum(num)
#     else:
#         answer -= int(x)
# print(answer)


# answer = sum(map(int, exp.pop(0).split('+'))) if '+' in exp[0] else int(exp.pop(0))