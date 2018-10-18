import random
import os
import time

carac = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

senha = ''

op = int(input('Quantos caracteres a senha deve ter: '))
print('\n')
os.system('cls')
for i in range(0, op):
    senha += carac[random.randint(0, len(carac) - 1)]
print(senha)
time.sleep(2)
