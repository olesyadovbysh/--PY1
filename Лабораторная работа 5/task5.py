import random
import string

def get_random_password(n=8) -> str:
    alphabet = string.ascii_letters + string.digits
    password_list = random.sample(alphabet, n)
    password = ''.join([str(num) for num in password_list])
    return password

print(get_random_password())
