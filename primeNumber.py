def get_prime_numbers(number):
    if (number < 1) : return
    s = []
    for i in range(2, number+1):
        prime = True
        for j in range(2,i):
            if (i % j == 0):
                prime = False
                break
        if prime: s.append(i)
    return s

result = get_prime_numbers(5)
print (result)