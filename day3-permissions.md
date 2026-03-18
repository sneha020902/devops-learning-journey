Day3 - FILE PERMISSIONS

    chmod -> change file permissions

    ls -l -> shows permissions

PERMISSION TYPES:

      r- read

      w- wrire

      x- execute

EACH PERMISSION HAS A VALUE:

      r- 4

      w- 2

      x- 1

  EXAMPLE:

      rwx = 4+2+1 = 7

      rw- = 4+2 = 6

      r-- =4

USERS: owner | group | others

EXAMPLE:

      chmod +x file.sh -> make it executable

      chmod -x file.sh -> remove execution permissions

      chmod 777 file.sh -> full access

      chmod 644 file.txt -> standard file permission

WHAT IS 777?

      rwxrwxrwx 

      MEANS- Owner(rwx-7), Group(rwx-7), Others(rwx-7): everyone can read write and execute

WHAT IS 644"

      rw-r--r--

      MEANS- Owner(rw- -> 6), Group(r-- -> 4),  Others(r-- -> 4): Owner can read and write, others and group can only read. 

WHAT IS 755?

    rwxr-xr-x

    MEANS- It gives full permission to owner and read-execute permissions to group and others.
