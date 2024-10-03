import os
import time

source = ['/Users/js/notes']
target_dir = '/Users/js/backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # makr directory

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory
# in the main directory.
today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive.
now = time.strftime('%H%M%S')

# The name of the zip file
target = today + os.sep + now + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 5. We use the zip command to put the files in a zip archive
zip_command = 'zip -r {0} {1}'.format(target, 
                                    ' '.join(source))


# Run the backup
print('Zip command is:')
print(zip_commmand)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
