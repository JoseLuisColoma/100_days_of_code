
def prime_checker(number):
    for i in range(2, number):
        if n % i == 0:
            return print("It's not a prime number.")

    return print("It's a prime number.")



n = int(input())
prime_checker(number=n)