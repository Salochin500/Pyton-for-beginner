
#generate password which is hard to break for hackers

import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols= "@#$%&*/\?"

Use_for = lower_case + upper_case + number + symbols
length_for_pass = 8

password = "".join(random.sample(Use_for, lenght_for_pass))

print("Your Generated Password")
