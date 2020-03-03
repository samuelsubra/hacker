# Hacker
# Version 3

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

# determine outcome
if guess == 'HUNTING':
    outcome_line2 = 'EXITING DEBUG MODE'
    outcome_line3 = 'LOGIN SUCCESSFUL - WELCOME BACK'
    outcome_line4 = 'PRESS ENTER TO CONTINUE'
else:
    outcome_line2 = 'LOGIN FAILURE - TERMINAL LOCKED'
    outcome_line3 = 'PLEASE CONTACT AN ADMINISTRATOR'
    outcome_line4 = 'PRESS ENTER TO EXIT'

# display outcome
print(guess)
print('')
print(outcome_line2)
print('')
print(outcome_line3)
print('')
input(outcome_line4)
