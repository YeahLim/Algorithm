# 문자열 A와 B가 주어진다. 
# 한 번 문자열을 바꾸는 것은 A의 한 글자를 골라서 문자열의 가장 처음으로 옮기는 것을 의미한다.
# A를 B로 바꾸기 위해서 문자열을 바꿔야 하는 횟수의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A, 둘째 줄에 B가 주어진다. 두 문자열의 길이는 같으며, 길이는 50을 넘지 않는다. 또, 알파벳 대문자로만 이루어져 있다.

# 출력
# 첫째 줄에 A를 B로 바꾸는 연산 횟수의 최솟값을 출력한다. A를 B로 바꿀 수 없을 때는 -1을 출력한다.

from sys import stdin
init = stdin.readline()
tar = stdin.readline()
init_diff = []
tar_diff = []

for i in range(len(init)):
    if init[i]

# 끝에서 부터 비교하다가
# 다른게 나옴
# 그러면 tar은 뒤에서부터, init은 앞에서부터 비교