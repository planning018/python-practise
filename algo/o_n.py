

# 时间复杂度 O(1)
def O1(num):
    i = num
    j = num * 2
    return i + j


# 时间复杂度 O(logN)
def OlogN(num):
    i = 1
    while i < num:
        i = i * 2
    return i


# 时间复杂度 O(N)
def ON(num):
    total = 0
    for i in range(num):
        total += i
    return total


# 时间复杂度 O(M+N)
def OMN(num1, num2):
    total = 0
    for i in range(num1):
        total += i
    for j in range(num2):
        total += j
    return total


# 时间复杂度 O(NlogN)
def ONLogN(num1, num2):
    total = 0
    j = 0
    for i in range(num1):
        while(j < num2):
            total += i + j
            j = j * 2
    return total


# 时间复杂度 O(N2)
def ON2(num):
    total = 0
    for i in range(num):
        for j in range(num):
            total += i + j
    return total


