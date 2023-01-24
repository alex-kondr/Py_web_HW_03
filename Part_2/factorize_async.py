from time import time
import multiprocessing
from concurrent.futures import ProcessPoolExecutor


time_start = time()
CPU_COUNT = multiprocessing.cpu_count()

"""Divide a large number into numbers that are equal 'SEPARATOR'"""
SEPARATOR = 1000000


def factorize(separation_number, number):
    """Find list of divisors by number less than 'SEPARATOR'"""
    
    list_of_divisors = []
    
    if separation_number > SEPARATOR:
        for i in range(separation_number-SEPARATOR, separation_number+1):
            if not number % i:
                list_of_divisors.append(i)    
    else:
        for i in range(1, separation_number+1):
            if not separation_number % i:
                list_of_divisors.append(i)
                
    return list_of_divisors

def factorize_one_number(number):
    """Divides a number by more 'SEPARATOR'"""
    
    futures = []
    list_of_divisors = []
    
    separation_numbers = [i for i in range(1, number, SEPARATOR)
               if i > SEPARATOR] + [number]

    with ProcessPoolExecutor(CPU_COUNT*2 + 1) as executor:
        for separation_number in separation_numbers:
            futures.append(executor.submit(factorize, separation_number, number))
    
    for future in futures:
        list_of_divisors += future.result()
                    
    return list_of_divisors


def factorize_numbers(*numbers: int) -> list[int]:
    list_of_divisors = []

    for number in numbers:
        list_of_divisors.append(factorize_one_number(number))

    return list_of_divisors


if __name__ == "__main__":
    
    a, b, c, d = factorize_numbers(128, 255, 99999, 10651060)
    
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 
                 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    print(time()-time_start)