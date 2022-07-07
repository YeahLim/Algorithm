for _ in range(int(input())):
    applicants = []
    nums = int(input())
    for _ in range(nums):
        applicants.append(list(map(int, input().split())))
    applicants.sort()
    count = nums
    for i in range(1, nums):
        temp = applicants[i]
        for j in range(0, i):
            applicant = applicants[j]
            if temp[0] > applicant[0]:
                if temp[1] > applicant[1]: 
                    count -= 1
                    break
    print(count)

 