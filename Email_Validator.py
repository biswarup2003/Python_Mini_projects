email=input("Enter the email :  ") #biswarup.com   abc.gmail.com  abc.in
msg="correct"
if len(email)>=6:
    if(email[0].isalpha()):
        if("@" in email) and (email.count("@")==1):
            if(email[-4]==".") or (email[-3]=="."):
                for i in email:
                    if(i.isspace()):
                        msg="wrong 5"
                    elif(i.isupper()):
                        msg="wrong 6"
                    elif(i.isdigit()) or i=="_" or i=="@" :
                        continue
                    
            else:
                msg="wrong 4"
        else:
            msg="wrong 3"
    else:
        msg="wrong 2"
else:
    msg = "wrong 1"
    
print(f"Your email is {email} \n This is {msg}")