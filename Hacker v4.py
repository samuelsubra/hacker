# Hacker
# Version 4

# display header
header = ['DEBUG MODE', '1 ATTEMPT(S) LEFT', '']
for header_line in header:
    print(header_line)

# display passwords
passwords = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS', 'SURVIVE', 'HEARING', 'HUNTING', 'REALIZE', 'NOTHING', 'OVERLAP', 'FINDING', 'PUTTING', '']
for password_line in passwords:
        print(password_line)

# prompt user
guess = input('Enter password >')

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
