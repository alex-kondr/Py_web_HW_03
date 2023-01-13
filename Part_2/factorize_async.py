from time import time
import multiprocessing
from concurrent.futures import ProcessPoolExecutor


time_start = time()
CPU_COUNT = multiprocessing.cpu_count()
# temp = 0

"""Divide a large number into numbers that are equal 'SEPARATOR'"""
SEPARATOR = 1000000






def factorize_one_number(number):
    """Divides a number by more 'SEPARATOR'"""
    
    # global temp
    # temp = number
    # print(temp)
    list_of_divisors = []
    
    numbers = [i for i in range(1, number, SEPARATOR)
               if i > SEPARATOR] + [number]
    # print(numbers)

    with ProcessPoolExecutor(CPU_COUNT) as executor:
        for num in numbers:
            list_of_divisors += executor.submit(factorize, num, number)
        
        
        # for preliminary_list in executor.map(factorize, numbers):
        #     list_of_divisors += preliminary_list
            
    # print(list_of_divisors)
            
    return list_of_divisors


def factorize(num, number):
    """Find list of divisors by number less than 'SEPARATOR'"""
    # global temp
    test = []
    # print(temp)
    
    if num > SEPARATOR:
        for i in range(num-SEPARATOR, num+1):
            if not number % i:
                test.append(i)    
    else:
        for i in range(1, num+1):
            if not num % i:
                test.append(i)
                
    return test


def factorize_numbers(*numbers: int) -> list[int]:
    test1 = []

    for number in numbers:
        test1.append(factorize_one_number(number))

    return test1


if __name__ == "__main__":
    a = factorize_one_number(10651060)
    print(temp)
    
    # print(len(a))
    
    
    # a, b, c, d = factorize_numbers(128, 255, 99999, 10651060)
    
    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    
    # # print(d)
    
    # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
    #             380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    
    print(time()-time_start)