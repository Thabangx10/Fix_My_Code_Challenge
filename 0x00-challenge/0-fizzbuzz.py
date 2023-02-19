#!/usr/bin/python3
"""
FizzBuzz
"""
import sys


def fizzbuzz(n):
    """
    The function will be printing numbers seperated (1 from n)

    Multiples:
             3 - print "Fizz"
             5 - print "Buzz"
             both - print "FizzBuzz"
    Error:
             we needed to handle the error by calling the if loop that called
             both multiples first in the program.
    """
    if n < 1:
        return

    tmp_result = []
    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            temp_result.append("FizzBuzz")
        elif (i % 3) == 0:
            temp_result.append("Fizz")
        elif (i % 5) == 0:
            temp_result.append("Buzz")
        else:
            temp_result.append(str(i))
    print(" ".join(tmp_result))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys,argv[1])
    fizzbuzz(number)
