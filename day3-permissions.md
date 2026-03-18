Day3 - File Permissions

chmod -> change file permissions

ls -l -> shows permissions

Permission Types:

r- read

w- wrire

x- execute

Each permission has a vaue:

r- 4

w- 2

x- 1

rwx = 4+2+1 = 7

rw- = 4+2 = 6

r-- =4

Users:
owner | group | others

Example:

chmod +x file.sh -> make it executable

chmod -x file.sh -> remove execution permissions

chmod 777 file.sh -> full access

chmod 644 file.txt -> standard file permission

What is 777?

rwxrwxrwx 

Means- Owner(rwx-7), Group(rwx-7), Others(rwx-7): everyone can read write and execute

What is 644"

rw-r--r--

Means- Owner(rw- -> 6), Group(r-- -> 4),  Others(r-- -> 4): Owner can read and write, others and group can only read. 
