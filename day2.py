studentid=input("Enter Student ID:")
email=input("Enter Email id:")
password=input("Enter Password:")
refcode=input("Enter Referral Code:")

valid=True

if(len(studentid)!=7 or studentid[0:3]!="CSE" or studentid[3]!="-"
        or not(studentid[4].isdigit() and studentid[5].isdigit() and studentid[6].isdigit())):
    valid=False
    
elif(email.count("@")<1 or email.count(".")<1 or email[0]=="@" or email[len(email)-1]=="@"
          or email[len(email)-4:len(email)]!=".edu"):
    valid=False

elif(len(password)<8 or not("A"<=password[0]<="Z")
     or password.count('0') + password.count('1') + password.count('2') +
    password.count('3') + password.count('4') + password.count('5') +
    password.count('6') + password.count('7') + password.count('8') +
    password.count('9')<1):
    valid=False

elif(len(refcode)!=6 or refcode[0:3]!="REF" or not(refcode[3].isdigit() and refcode[4].isdigit())
     or refcode[5]!="@"):
    valid=False
    
if(valid):
    print("APPROVED")
else:
    print("REJECTED")