from operator import length_hint
import random 

print('WELCOME TO PASSWORD GENERATOR') 

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,.!?@#$%^&*()-_+=[]{}|\/:;"<>¡¿'

number = input('How many passwords do you want to generate: ')
number = int(number)

length = input('How much length do you want for yours passwords: ')
length = int(length)

print('\nYour passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords) 