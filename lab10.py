# exercise 1:


def bank_statement(L:list):
    """Takes a list of floating point numbers and sorts them into positives and negatives. The positives act as the
    bank deposits whilst the negatives act as the withdrawals. The function then returns a new list contain total
    deposits, withdrawals, and balance.
    >>>bank_statement([2.3, 4.5, -4.12])
    [6.8, -4.12, 2.68]
    >>>bank_statement([8.12,-16.2,2.30])
    [10.42, -16.2, -5.78]
    """
    deposits = 0
    withdrawal = 0
    for i in L:
        if i >= 0:
            deposits += i
        elif i < 0:
            withdrawal += i
    return [round(deposits,2), round(withdrawal,2), round(deposits+withdrawal,2)]


test = bank_statement([5.3, 6.975748, -2.234, -3.23409452312])
print(test)

print('----------------------------------------------------------------------------')

# exercise 2:


def divisors(num: int):
    """Takes a number and returns a list containing all of its divisors
    >>>divisors(5)
    [1,5]
    >>>divisors(6)
    [1,2,3,6]
    >>>divisors(8)
    [1,2,4,8]
    """
    divs = []
    for i in range(1, num):
        if num % i == 0:
            divs.insert(i-1, i)
    divs.insert(len(divs), num)
    return divs


test = divisors(8)
print(test)

print('----------------------------------------------------------------------------')

# exercise 3:


def reverse(L:list):
    """Takes a list and reverses the order of the elements
    >>>reverse([1,2,3,4,5])
    [5,4,3,2,1]
    >>>reverse([12,15,14,13,11])
    [11,13,14,15,12]
    """
    counter = 0
    N = []
    for i in L:
        N.insert(-1-counter, i)
        counter += 1
    return N


test = reverse([1,2,3,4,5,6,7,8,9,0])
print(test)
