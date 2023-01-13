from time import time


time_start = time()


def factorize(*numbers: int) -> list[int]:
    list_of_divisors = []

    for number in numbers:
        list_of_divisors_for_number = []

        for i in range(1, number+1):
            if not number % i:
                list_of_divisors_for_number.append(i)

        list_of_divisors.append(list_of_divisors_for_number)

    return list_of_divisors


a, b, c, d = factorize(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
             380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

print(time()-time_start)
