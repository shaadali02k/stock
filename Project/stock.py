num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

import random
import string

password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
print("Generated Password:", password)


