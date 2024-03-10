# 多进程和进程池

import concurrent.futures
import math
import multiprocessing

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    """是否为素数"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number in PRIMES:
            future = executor.submit(is_prime,number)
            print(f'{multiprocessing.current_process().name} {number} is prime : {future.result()}')
    # for future in futures:
    #     print(future.result())
        # for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
        #     print(f'{multiprocessing.current_process().name} {number} is prime: {prime}')

if __name__ == '__main__':
    main()
