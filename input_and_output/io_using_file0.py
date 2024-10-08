poem = '''\
Programming is fun
When the work is down
if you wanna make your work also fun:
	use python!
'''


# Open for 'w'riting
f = open('poem.txt', 'w')
# Write text to file 
f.write(poem)
# Close the file 
f.close()

# If no mode is spexified,
# 'r'ead mode is assumed by default
f = open('poem.txt')
while True:
    line = f.readline()
    # Zero length indicates EOF 
    if len(line) == 0:
        break
    # The `line` already has a newline 
    # at the end of each line
    # since it is reading from a file. 
    print(line, end='')
# close the file 
f.close()
