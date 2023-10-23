##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied

example:
example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 1234
Access denied
Too many failed attempts. Access denied.
"""

username = ("admin")


count = 0

while count < 3:
    
    user = input("Username: ")
    password = input("Password: ")
    if user != "admin" and password != "12345":
        print("access denied")
        
    elif user == "admin" and password == "12345":
        print("Access granted")
        break
else:
    print("Too many tries")
   
    