def factorial_of(num):
    if num == 1:
        return 1;
    else:
        return num * factorial_of(num-1)
    
print(factorial_of(5))




def while_fac(num):
    factorial = 1
    while num > 1:
        factorial*=num
        num -=1

    return factorial


print(while_fac(5))



# 0 1 1 2 3 5 8 13

def fibonacci_of(num):
    if num in {0, 1}:  # Base case
        return num
    return fibonacci_of(num-1) + fibonacci_of(num-2)

fibonacci_sequence = [fibonacci_of(n) for n in range(15)]
print(fibonacci_sequence)