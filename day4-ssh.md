Day 4 - SSH  (Secure Shell)

What is SSH?

        (Secure Shell) It allows you to work on another remote server through your laptop.
        ssh - connect to remote server

Example:

        ssh username@server-ip (ssh ubuntu@1.2.3.4)

SSH is used to:

    -> connect to servers
    -> manage cloud instances
    -> deploy applications

Steps:

    1. Create key pairs
    2. Connect using SSH
    3. Run commands on server

Commands with their meaning:

  1- 'ssh-keygen'- Generate SSH Key(after clicking "enter" for everything asked after this. Two keys will be generated                     id_abc and id_abc.pub.
                   'id_abc' - private key (keep secret)
                   'id_abc.pub' - public key (share)
  2- 'cat ~/.ssh/id_abc.pub' - to view your public key

What is the use of this key?
    When we launch your AWS server: We use this key to login
  

