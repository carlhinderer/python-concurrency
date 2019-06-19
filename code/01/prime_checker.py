from math import sqrt
from timeit import default_timer as timer
import concurrent.futures

def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False

    limit = int(sqrt(x)) + 1
    for i in range(3, limit, 2):
        if x % i == 0:
            return False

    return True


def check_primes_sequentially(prime_list):
    start = timer()
    result = []
    for i in prime_list:
        if is_prime(i):
            result.append(i)
    print('Result 1:', result)
    print('Took: %.2f seconds.' % (timer() - start))


def check_primes_concurrently(prime_list):
    start = timer()
    result = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(is_prime, i) for i in prime_list]
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            if future.result():
                result.append(prime_list[i])

    print('Result 2:', result)
    print('Took: %.2f seconds.' % (timer() - start))


def run_performance_test():
    primes = [i for i in range(10 ** 13, 10 ** 13 + 500)]
    check_primes_sequentially(primes)
    check_primes_concurrently(primes)


if __name__ == '__main__':
    run_performance_test()