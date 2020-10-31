

def accumulated_amount(principal, rate, n, time):
    return principal*(1+(rate/n))**(n*time)

amount = accumulated_amount(10,2,1,2)
print(amount)
amount = accumulated_amount(10.0,2.0,1.0,2.0)
print(amount)
amount = accumulated_amount(1500,0.3,2,2)
print(amount)
amount = accumulated_amount(1500.0,0.3,2.0,2.0)
print(amount)
amount = accumulated_amount(0,2,1,2)
print(amount)
amount = accumulated_amount(10,0,1,2)
print(amount)