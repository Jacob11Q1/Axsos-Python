# 1) Biggie Size
def biggieSize(list):
    for x in range(len(list)):
        if list[x] > 0:
            list[x] = "Big"
    return list
l1 = [2,3,-7,5,-1,6]
print(biggieSize(l1))

# 2) Positive Numbers
l1 = [2,3,-7,5,-1,6]
def countPositive(list):
    counter = 0
    for x in range(len(list)):
        if list[x] > 0:
            counter += 1
        list[-1] = counter #list[list(list) -1]
    return list
print(countPositive(l1))

# 3) Sum Total
def sumTotal(list):
    total = 0
    for x in list:
        total += x
    return total
list = [2,3,4,1,2]
print(sumTotal(list))

# 4) Average
def average(list):
    total = 0
    for x in list:
        total += x
    avg = total / len(list)
    return avg
l3 = [2,2,4,8,6]
print(average(l3))

# 5) Length
def length(list):
    counter = 0
    for x in range(len(list)):
        counter += 1
    return counter
l5 = [5,7,8,9,6,7,1]
print(length(l5))

# 6) Minimum
def minimum(list):
    if len(list) == 0:
        return False
    else:
        min = list[0]
        for x in list:
            if x < min:
                min = x
        return min
lMin = [8,9,6,4,-7,5,2,4,7]
lMin1 = []
print(minimum(lMin))
print(minimum(lMin1))

# 7) Maximum
def maximum(list):
    if len(list) == 0:
        return False
    else:
        max = list[0]
        for x in list:
            if x > max:
                max = x
        return max
lMin = [8,9,6,4,-7,5,2,4,7]
lMin1 = []
print(maximum(lMin))
print(maximum(lMin1))

# 8) Ultimate Analysis
def dictionary(list):
    dic = {
        "sumTotal":sumTotal(list),
        "Average":average(list),
        "Minimum":minimum(list),
        "Maximum":maximum(list),
        "Length":length(list)
    }
    return dic
list8 = [1,5,3,1]
print(dictionary(list8))

# 9) Reverse List
def reverse_list(x):
    for i in range(len(x)//2):
        x[i],x[-1-i]=x[-1-i],x[i]
    return x

print(reverse_list([6,4,9,2,1,7,-2,6,]))