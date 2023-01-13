from time import time
import multiprocessing
from concurrent.futures import ProcessPoolExecutor


time_start = time()
CPU_COUNT = multiprocessing.cpu_count()
SEPARATOR = 1000000
temp = 0


def factorize(number):
    preliminary_list = []
    
    if number > SEPARATOR:
        for i in range(number-SEPARATOR, number+1):
            if not temp % i:
                preliminary_list.append(i)        
    
    else:
        for i in range(1, number+1):
            if not number % i:
                preliminary_list.append(i)
                
    return preliminary_list


def factorize_one_number(number):
    global temp
    temp = number
    
    numbers = [i for i in range(1, number, SEPARATOR)
               if i > SEPARATOR] + [number]
    list_of_divisors = []

    with ProcessPoolExecutor(CPU_COUNT) as executor:
        for preliminary_list in executor.map(factorize, numbers):
            list_of_divisors += preliminary_list
            
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