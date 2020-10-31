# exercise 1:


def count_evens(list:list):
    """Counts the number of elements that are even
    >>>count_evens([1,3,5,7])
    0
    >>>count_evens([2,4,6,8])
    4
    >>>count_evens([9,4,0,8])
    3
    """
    count = 0
    for x in list:
        if x % 2 == 0:
            count += 1
    return count


def test_count_evens(expected:int, l:list):
    print('Testing count_evens', l)
    print('Expected Value:', expected, ', Actual Value:', count_evens(l))
    if expected == count_evens(l):
        return 'Successful'
    else:
        return 'Failed'


test = test_count_evens(2,[1,2,3,4])
print(test)
test = test_count_evens(4,[2,4,6,8])
print(test)
test = test_count_evens(0,[1,3,5,7,9,11,13,15])
print(test)

print('-------------------------------------------------')
# exercise 2:


def big_diff(L:list):
    """Finds the difference between the largest element and the smallest element of the list.
    >>>big_diff([1,2,3])
    2
    >>>big_diff([10,11,12,16])
    6
    """
    x = 0
    y = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    for i in L:
        if x < i:
            x = i
        elif y > i:
            y = i
    return x - y

def test_big_diff(expected:int, l:list):
    print('Testing count_evens', l)
    print('Expected Value:', expected, ', Actual Value:', big_diff(l))
    if expected == big_diff(l):
        return 'Successful'
    else:
        return 'Failed'


test = test_big_diff(9,[11,2,3])
print(test)
test = test_big_diff(2,[3,2,1])
print(test)
test = test_big_diff(5,[10,5,6,8])
print(test)

print('-------------------------------------------------')
# exercise 3:


def has22(list:list):
    """If function has 2 2s side by side, returns true else false
    >>>has22([1,2,2,1])
    True
    >>>has22([1,2,3,42,3,4])
    False
    >>>has22([2,1,3,2,4,2,2])
    True
    """
    for i in range(len(list)-1):
        if list[i] == 2:
            if list[i+1] == 2:
                return True
    return False

def test_has22(expected, l:list):
    print('Testing count_evens', l)
    print('Expected Value:', expected, ', Actual Value:', has22(l))
    if expected == has22(l):
        return 'Successful'
    else:
        return 'Failed'

test = test_has22(False,[1,1,1,1,1,1,1,2])
print(test)
test = test_has22(False,[1,3,4,5,5,6,7,7,8])
print(test)
test = test_has22(True,[1,2,2,3,4,5])
print(test)
test = test_has22(True,[1,2,1,1,2,1,2,2])
print(test)

print('-------------------------------------------------')
# exercise 4:


def centered_average(L:list):
    """Finds the average of the list consisting of all elements except the max and min.
    >>>centered_average([1,2,3,4])
    2.5
    >>>centered_average([10,11,12,13])
    11.5
    >>>centered_average([23,21,1,14,5])
    13.3333333333333333333
    """
    x = 0
    for i in L:
        x += i
    return (x - min(L) - max(L))/(len(L)-2)

def test_centered_average(expected:float, l:list):
    print('Testing count_evens', l)
    print('Expected Value:', expected, ', Actual Value:', centered_average(l))
    if expected == centered_average(l):
        return 'Successful'
    else:
        return 'Failed'


test = test_centered_average(2.5,[1,2,3,4])
print(test)
test = test_centered_average(15.0,[10,12,14,16,18,20])
print(test)
test = test_centered_average(8.2,[21,3,4,5,1,61,8])
print(test)