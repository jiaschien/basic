import os
import time

# 1. The files and directories to be backed up are
# specified in a list.
# Example on Windows:
source = ['/Users/js/notes']
# Notice we had to use double quotes inside the string
# for names with spaces in it.

target_dir = '/Users/js/backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # makr directory

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory
# in the main directory.
today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive.
now = time.strftime('%H%M%S')

# Take a comment from the user to
# create the name of the zip file
comment = input('Enter a comment --> ')
# Check if a comment was entered
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + 
        comment.replace(' ', '_') + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exsits(today):
    os.mkdir(today)
    print('Sucessfully created directory', today)


# 5. We use the zip command to put the files in a zip archive
zip_command = "zip -r {0} {1}".format(target,
                                    ' '.join(source))


# Run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

