import string
import random


def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))
print("Welcome to PassWord Generator - Enter Password Lenght You Want and Get Your Passowrd")
print(pw_gen(int(input('How many characters in your password?'))))
