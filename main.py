from random import randint, choice
numbers = [str(i) for i in range(10)]
big_alpha = [chr(i) for i in range(65, 91)]
low_alpha = [chr(i) for i in range(141, 173)]
symbol = list('@#$?!&')

sign = {1:numbers , 2:big_alpha, 3:low_alpha, 4:symbol}

password = ''
length = randint(8,15)
for i in range(length):
    password += choice(sign[randint(1,4)])
    
print(password)
