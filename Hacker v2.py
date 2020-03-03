# Hacker
# Version 2

# display header
print('DEBUG MODE')
print('1 ATTEMPT(S) LEFT')
print('')

# display passwords
print('PROVIDE')
print('SETTING')
print('CANTINA')
print('CUTTING')
print('HUNTERS')
print('SURVIVE')
print('HEARING')
print('HUNTING')
print('REALIZE')
print('NOTHING')
print('OVERLAP')
print('FINDING')
print('PUTTING')
print('')

# prompt user
guess = input('Enter password >')

# display outcome
if guess == 'HUNTING':
    print(guess)
    print('')
    print('EXITING DEBUG MODE')
    print('')
    print('LOGIN SUCCESSFUL - WELCOME BACK')
    print('')
    input('PRESS ENTER TO CONTINUE')
else:
    print(guess)
    print('')
    print('LOGIN FAILURE - TERMINAL LOCKED')
    print('')
    print('PLEASE CONTACT AN ADMINISTRATOR')
    print('')
    input('PRESS ENTER TO EXIT')
