import random

print("Welcome to Password Generator!")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

while True:
    try:
        number = int(input('Amount of passwords to generate: '))
        length = int(input('Input your password length: '))

        print('\nHere are your passwords:\n')
        for _ in range(number):
            password = ''.join(random.choice(chars) for _ in range(length))
            print(password)

        print('\nThank you for using Password Generator!')

    except ValueError:
        print("Please enter valid numerical values for the amount and length.")

    inp = input("\nTo quit, press 'Y'. To generate more passwords, press any other key: ").strip().lower()
    if inp == 'y' or 'Y':
        print("Goodbye!")
        break