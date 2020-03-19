# Hacker
# Version 5

# display header
attempts = 4
header = ['DEBUG MODE', str(attempts) + ' ATTEMPT(S) LEFT', '']
for header_line in header:
    print(header_line)

# display passwords
passwords = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS', 'SURVIVE', 'HEARING', 'HUNTING', 'REALIZE', 'NOTHING', 'OVERLAP', 'FINDING', 'PUTTING', '']
for password_line in passwords:
        print(password_line)

# prompt
guess = input('ENTER PASSWORD >')
attempts = attempts - 1

# haven't guessed it yet and still have guesses
while (guess != 'HUNTING') and (attempts > 0):
    print(str(attempts) + ' ATTEMPT(S) LEFT')
    if attempts == 1:
        print('*** LOCKOUT WARNING ***')
    guess = input('ENTER PASSWORD >')
    attempts = attempts - 1

# determine outcome
if guess == 'HUNTING':
     outcome = [guess, '', 'EXITING DEBUG MODE', '', 'LOGIN SUCCESSFUL - WELCOME BACK', '']
     final = 'PRESS ENTER TO CONTINUE'
else:
     outcome = [guess, '', 'LOGIN FAILURE - TERMINAL LOCKED', '', 'PLEASE CONTACT AN ADMINISTRATOR', '']
     final = 'PRESS ENTER TO EXIT'

# display outcome
for outcome_line in outcome:
    print(outcome_line)
input(final)
