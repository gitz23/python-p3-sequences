#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = [0,1] #initiallizing the empty arr

    for num in range(2, length): #for each num in the range starting from 2 and max being inputted len
        print(num)
        next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2] #adds the last num to the second-last num in the seq to get the next
        fibonacci_sequence.append(next_num)

    return(fibonacci_sequence)
print(print_fibonacci(10))
