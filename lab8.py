# exercise 1:


def first_last6(nums:list):
    """Returns true or false depending on whether the first and/or last number is 6
    >>>first_last6([1,2,3,4,5,6])
    True
    >>>first_last6([6,5,4,3,2,1])
    True
    >>>first_last6([5,6,6,6,6,5])
    False
    >>>first_last6([1,2,3,4,5,3,3,2,1])
    False
    """
    a = len(nums)
    if nums[0] == 6 or nums[a-1] == 6:
        return True
    else:
        return False


test = first_last6([6, 1, 1, 1, 1])
print(test)
test = first_last6([11, 1, 1, 2, 3, 6])
print(test)
test = first_last6([1, 6, 6, 6, 6, 6, 1])
print(test)


print('-------------------------------------------------')
# exercise 2:


def same_first_last(L:list):
    """Returns True if the list is not empty and the first and last number are equal.
    >>>same_first_last([])
    False
    >>>same_first_last([1,2,3,4])
    False
    >>>same_first_last([1,2,3,1])
    True
    """
    if L == []:
        return False
    if L[0] == L[len(L)-1]:
        return True
    else:
        return False


test = same_first_last([1, 2, 3, 1])
print(test)
test = same_first_last([])
print(test)
test = same_first_last([2, 3, 4, 1, 4])
print(test)

print('-------------------------------------------------')
# exercise 3:


def make_pi(pi:list):
    """ Returns true if a list of 3 has the elements containing 3,1,4
    >>>make_pi(3,1,4)
    True
    >>>make_pi(4,1,3)
    False
    """
    if len(pi) == 3:
        if pi[0] == 3 and pi[1] == 1 and pi[2] == 4:
            return True
        else:
            return False
    else:
        return False
    return [3,1,4]


test = make_pi([3,1,4,6])
print(test)
test = make_pi([3,1,4])
print(test)
test = make_pi([1,2,3,4])
print(test)

print('-------------------------------------------------')
# exercise 4:


def common_end(list1:list,list2:list):
    """Returns True if the lists contain the same last element and/or same first element
    >>>common_end([1,2,3],[3,2,1])
    True
    >>>common_end([2,3,4,5,6])
    False
    >>>common_end([1,2,3,4,5,6],[1,0,9,8,7])
    True
    """
    if list1[len(list1)-1] == list2[len(list2)-1]:
        return True
    if list1[len(list1)-1] == list2[0]:
        return True
    if list1[0] == list2[len(list2)-1]:
        return True
    if list1[0] == list2[0]:
        return True
    else:
        return False


test = common_end([1,2,3,1,2,3],[2,2,2,2,2,3])
print(test)
test = common_end([1,2,3,4,5,6],[1,0,9,8,7])
print(test)
test = common_end([1,3,4,5,6,7,8],[8,7,6,5,4,3,2,1])
print(test)
test = common_end([3,2,1],[7,1,4])
print(test)

print('-------------------------------------------------')
# exercise 5:


def sum3(list:list):
    """Returns the sum for the elements of a list containing 3 integers.
    >>>sum3([1,2,3])
    6
    >>>sum3([12,13,15])
    40
    >>>sum3([1,1,1])
    3
    """
    return list[0]+list[1]+list[2]


test = sum3([4,5,6])
print(test)
test = sum3([7,8,19])
print(test)
test = sum3([102,231,590])
print(test)

print('-------------------------------------------------')
# exercise 6:


def rotate_left3(rotate:list):
    """Takes a 3 elements list and returns a new list with the same elements but shifted to the left.
    >>>rotate([1,2,3])
    [2,3,1]
    >>>rotate([24,32,1])
    [32,1,24]
    """
    if len(rotate) == 3:
        x = rotate[0]
        y = rotate[1]
        z = rotate[2]
        rotate[0] = y
        rotate[1] = z
        rotate[2] = x
        return rotate
    else:
        return 'List requires only 3 elements'


test = rotate_left3([1, 2, 3])
print(test)
test = rotate_left3([1, 2, 3, 4])
print(test)
test = rotate_left3([21, 104, 54])
print(test)

print('-------------------------------------------------')
# exercise 7:


def reverse3(reverse:list):
    """Takes a 3 element list and swaps the first and last element.
    >>>reverse3([1,2,3])
    [3,2,1]
    >>>reverse3([12,61,45])
    [45,61,12]
    """
    if len(reverse) == 3:
        x = reverse[0]
        y = reverse[2]
        reverse[0] = y
        reverse[2] = x
        return reverse
    else:
        return 'List requires 3 elements only'


test = reverse3([1, 2, 3])
print(test)
test = reverse3([3,6,2])
print(test)

print('-------------------------------------------------')
# exercise 8:


def max_end3(L:list):
    """Compares the first and last element of the list and converts all the elements into the largest of the 2
    >>>max_end3([1,2,3])
    [3,3,3]
    >>>max_end3([12,1,9])
    [12,12,12]
    """
    if len(L) ==3:
        if L[0] > L[2]:
            L[1] = L[0]
            L[2] = L[0]
            return L
        else:
            L[0] = L[2]
            L[1] = L[2]
            return L
    else:
        return 'List requires 3 elements only'


test = max_end3([1,2,3])
print(test)
test = max_end3([20,1,2])
print(test)

print('-------------------------------------------------')
# exercise 9:


def sum2(list1:list,list2:list):
    """Takes the first 2 elements of 2 lists and adds them together if the 2 lists contain more then 1 element
    >>>sum2([1,2],[3,4])
    4
    >>>sum2([1],[2,3])
    0
    >>>sum2([5,12],[10,9])
    15
    """
    if len(list1) == 1:
        return 0
    if len(list2) == 1:
        return 0
    else:
        return list1[0] + list2[0]


test = sum2([1],[1,2])
print(test)
test = sum2([3,5],[6,2,4,8,2,12])
print(test)
test = sum2([315,32,15,61],[81,92,3,5])
print(test)

print('-------------------------------------------------')
# exercise 10:


def middle_way(list1:list,list2:list):
    """Takes 2 lists and returns a new list containing the 2 middle elements
    >>>middle_way([5,4,6],[2,3,4])
    [4,3}
    >>>middle_way([6,21,31],[51,2,6])
    [21,2]
    """
    if len(list1) >= 4:
        return 'List can not contain more then 3 elements'
    if len(list2) >= 4:
        return 'List can not contain more then 3 elements'
    return [list1[1],list2[1]]


test = middle_way([1,2,3],[3,2,1])
print(test)
test = middle_way([4,6,1],[4,9,0])
print(test)
test = middle_way([1,2,3,4],[1,2,3])
print(test)

print('-------------------------------------------------')
# exercise 11:


def make_ends(L:list):
    """Returns a new list containing the first and last element of a list
    >>>make_ends([1,3,4,12,3])
    [1,3]
    >>>make_ends([31,64,68,345,29,889,12])
    [31,12]
    """
    return [L[0],L[len(L)-1]]


test = make_ends([1,2,3])
print(test)
test = make_ends([2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3])
print(test)
test = make_ends([12,413,61,69,350,65])
print(test)

print('-------------------------------------------------')
# exercise 12:


def has23(L:list):
    """Returns true if a list contains 2 or 3 as one of their elements
    >>>has23([3,2,4,1])
    True
    >>>has23([2,4,5,6])
    True
    >>>has23([3,4,5,6])
    True
    >>>has23([6,7,8,9])
    False
    """
    if 2 in L:
        return True
    if 3 in L:
        return True
    else:
        return False


test = has23([3,4,2,1])
print(test)
test = has23([1,1,1,1,2])
print(test)
test = has23([4,3,5,1,0])
print(test)
test = has23([1,4,5,6,7,8])
print(test)
