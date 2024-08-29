import re
email_condition = r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
email=input("Enter Email : ") 
print(f"Your Emaili is : {email}")
if re.search(email_condition,email):
    print("This is a Valid Email")
else:
    print("This is an Invalid Email")