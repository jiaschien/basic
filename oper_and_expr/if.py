num = 23
guess = int(input('Enter an integer : '))

if guess == num:
    # New block starts here.
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # New block ends here
elif guess < num:
    # Another block
    print('No it is a little higher than that')
    # You want do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have guessed > number to reach here

print('Done')
# This last statement is always executed,
# after the if statement is executed.
