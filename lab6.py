# excersise 1
def factorial(n: int) -> int:
    """Return n! for
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    positive values of n.
    """
    fact: int = 1
    for i in range(2, n+1):
        fact = fact * n
    return fact

def test_int(actual:int,expected:int):
    print('Running automated testing...')
    print('Expected result:',expected, ', Actual result:',actual)
    if actual == expected:
        print('successful')
        test_int.counter += 1
    else:
        print('failed')
    print('total successful tests:', test_int.counter)

test_int.counter = 0

test = test_int(factorial(1),1)
test = test_int(factorial(2),2)
test = test_int(factorial(3),6)
test = test_int(factorial(4),24)

print('-----------------------------------------------------')
# excersise 2
def tip(cost, satisfaction):
    """Return estimated tips depending on customer satisfaction, 20% for full satisfaction, 15% for moderate satisfaction
    5% for dissatisfied
    >>>tip(15,3)
    3.0
    >>>tip(20,2)
    3.0
    >>>tip(25,1)
    1.25
    """
    if satisfaction == 3:
        return cost*0.2
    if satisfaction == 2:
        return cost*0.15
    elif satisfaction == 1:
        return cost*0.05


x = 0
y = 0

test = tip(15,3)
print('testing tip(15,3)')
print('Expected result: 3.0, Actual result:', test)

if test == 3.0:
    print('successful')
    x += 1
else:
    print('failed')
    y += 1

test = tip(20,2)

print('testing tip(20,2)')
print('Expected result: 3.0, Actual result:', test)
if test == 3.0:
    print('successful')
    x += 1
else:
    print('failed')
    y += 1

test = tip (25,1)
print('testing tip(25.1)')
print('Expected result:1.5, Actual result:', test)

if test == 1.25:
    print('successful')
    x += 1
else:
    print('failed')
    y += 1

print('Successful excersise 2 tests:', x)
print('Failed excersise 2 tests:', y)

print('-----------------------------------------------------')
# excersise 3
def coupon(spent):
    """Returns the value of the coupon based on the amount spent in groceries. If spent < 10 then there is no coupon,
    if 10 < spent <= 60 its 8%, if 60 < spent <= 150 its 10%, if 150 < spent <= 210 its 12%, if spent > 210 its 14%
    >>>coupon(5)
    0
    >>>coupon(100)
    10.0
    >>>coupon(150)
    15.0
    >>>coupon(200)
    24.0
    >>>coupon(250)
    35.0
    """
    if spent < 10:
        return 0
    if spent <= 60:
        return spent*0.08
    if 60 < spent <= 150:
        return spent*0.10
    if 150 < spent <= 210:
        return spent*0.12
    if spent > 210:
        return spent*0.14


x = 0
y = 0

test = coupon(5)
print('testing coupon(5)')
print('Expected result: 0, Actual result:', test)
if test == 0:
    print('successful')
    x += 1
else:
    print('failed')
    y += 1

test = coupon(100)
print('testing coupon(100)')
print('Expected result: 10.0, Actual result', test)
if test == 10.0:
    print('successful')
    x += 1
else:
    print('failed')
    y += 1

test = coupon(150)
print("testing coupon(150)")
print('Expected result: 15.0, Actual result:', test)
if test == 15.0:
    print('succesful')
    x += 1
else:
    print('failed')
    y += 1

test = coupon(200)
print("testing coupon(200)")
print('Expected result: 24.0, Actual result:', test)
if test == 24.0:
    print('succesful')
    x += 1
else:
    print('failed')
    y += 1

test = coupon(250)
print("testing coupon(250)")
print('Expected result: 35.0, Actual result:', test)
if test == 35.0:
    print('succesful')
    x += 1
else:
    print('failed')
    y += 1

print('Successful excersise 3 tests:', x)
print('Failed excersise 3 tests:', y)