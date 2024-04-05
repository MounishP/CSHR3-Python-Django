givenname = "madam"
reversename =""

for i in givenname:
    reversename = reversename+i

if(givenname == reversename):
        print("given name", givenname, "is a palindrome")
else:
        print("given name", givenname, " is not a palindrome")
