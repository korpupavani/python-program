"""
when the condition in "if" block failed the elif
block is executed..
syntax:
if condition:
    statements
elif condition:
    statements
else:
    statements
"""
#checking the userid and password
userid = input("enter your userid..")
password = input("enter your password...")

if userid=="abc12345" and password=="pavithra@12345":
    print("welcome to our netbanking of summi bank")
elif userid=="korpu pavani" and password=="pavani@12345":
    print("welcome to your net banking of sai bank")
else:
    print("the userid and password is incorrect...try again")
    

