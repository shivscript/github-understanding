# Note: this is for learning purpose

# learn to use github
# very first example

print("Hello World")

# write a program to check whether prime or not
def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True