# exercise 1

def bakers_party(pastries:int, day:str):
    """Returns if the bakers party is successful or not based on the day of the week and the number of pastries
    >>>bakers_party(39,'monday')
    False
    >>>bakers_party(63,'sunday')
    True
    >>>bakers_party(69,'tuesday')
    False
    >>>bakers_party(55,'friday')
    True
    """
    weekday = ['monday', 'tuesday', 'wednesday', 'thursday']
    return (40 <= pastries <= 60) if day in weekday else (pastries <= 40)


test = bakers_party(40, 'monday')
print(test)
test = bakers_party(16, 'friday')
print(test)
test = bakers_party(64,'saturday')
print(test)

print('----------------------------------------------------------')

# exercise 2

def squirrel_play(temp:float, summer:bool):
    """ Returns if the squirrels go out and play depending on the temperature and if it is summer or not.
    >>>squirrel_play(75,False)
    True
    >>>squirrel_play(35,True)
    False
    """
    return (60.0 <= temp <= 100) if summer else (60.0 <= temp <= 90)


test = squirrel_play(70, True)
print(test)
test = squirrel_play(34, False)
print(test)
test = squirrel_play(101, True)
print(test)

print('----------------------------------------------------------')

# exercise 3

def great_42(num1:int, num2:int):
    """Returns true or false depending on if the 2 parameters are 42, have a sum of 42, or difference of 42.
    >>>great_42(42,1)
    True
    >>>great_42(32,10)
    True
    >>>great_42(43,1)
    True
    >>>great_42(1,2)
    False
    """
    if num1 or num2 == 42:
        return True
    else:
        if num1+num2 == 42:
            return True
        if abs(num2-num1) == 42:
            return True
        else:
            return False


test = great_42(42, 1)
print(test)
test = great_42(32, 10)
print(test)
test = great_42(43, 1)
print(test)
test = great_42(0, 4)
print(test)

print('----------------------------------------------------------')

# exercise 4
def blackjack(a:int, b:int):
    """Returns the variable closet to 21. However variables above 21 will return a 0.
    >>>blackjack(2,19)
    19
    >>>blackjack(26,2)
    2
    >>>blackjack(24,23)
    0
    """
    if b > 21:
        b = 0
    if a > 21:
        a = 0
    if a or b <= 21:
        if b <= a <= 21:
            return a
        elif a <= b <= 21:
            return b

test = blackjack(2, 55)
print(test)
test = blackjack(21, 22)
print(test)
test = blackjack(24, 23)
print(test)

print('----------------------------------------------------------')

# exercise 5
def sum_uniques(a, b, c):
    """Returns the sum of 3 unique numbers. If the number is the same it will not towards the summation.
    >>>sum_uniques(1, 2 ,3)
    6
    >>>sum_uniques(5, 5, 4)
    9
    >>>sum_uniques(2, 2, 2)
    0
    """
    if a == c == b:
        a = 0
        b = 0
        c = 0
    elif a == c:
        a = 0
    elif a == b:
        b = 0
    elif b == c:
        c = 0
    return a+b+c


test = sum_uniques(1, 10, 2)
print(test)
test = sum_uniques(3, 3, 3)
print(test)
test = sum_uniques(5, 5, 4)
print(test)
