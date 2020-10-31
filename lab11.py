# exercise 2:


def average(l:list) -> list:
    total = 0
    for i in l:
        for x in i:
            total += x
        avg = total/3
        print(avg)
        
    return l


test = average([(1, 2, 3), (4, 5, 6)])
print(test)


# exercise 4: