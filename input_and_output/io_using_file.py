poem = '''\
    Programming is fun
    When the work is done
    if you wanna make your work also fun:
        use Python!
'''

# Open for 'W'riting
f = open('poem.txt', 'w')
# write text to file
f.write(poem)
# Close the file
f.close()

# If no mode is specified,
# 'r'ead mode is assumed by default
f = open('poem.txt')
while True:
    line = f.readline()
    # 零长度文件表示 EOF
    if len(line) == 0:
        break
    # The line already has a newline
    # at the end of each line
    # since it is readling from a file.
    print(line, end='')
# close the file
f.close()
