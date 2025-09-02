# 1) CountDown from 5 like this and return [5,4,3,2,1]
def countdown(num):
    if num < 0:
        return [];
    return list(range(num , 0 , -1));
print(countdown(5));

# 2) Print And Return
def printNumbers(x,y):
    print(x)
    return(y)
print(printNumbers(5,8))

# 3) First Plus Length
def first_plus_length(listNum):
    return listNum[0] + len(listNum)
first_list = first_plus_length([1,2,3,4,5])
print(first_list)

# 4) Values Greater Than Second
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    sec = list[1]
    vgts = []
    
    for i in list:
        if i > sec:
            vgts.append(i)
    print(len(vgts))
    return(vgts)

print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([3]))

# 5) This Length , That Value
def length_and_value(size , value):
    return [value] * size
print(length_and_value(4, 7))
print(length_and_value(6, 2))