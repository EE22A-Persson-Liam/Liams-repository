corrPass = "password"
corrUser = "Liam"

username = input("username: ")
password = input("password: ")

username= username.lower()

if (username == corrUser):
    print("correct user: " + corrUser)
    if (password == corrPass):
        print("correct password: " + corrPass)
    else:
        print("wrong password")


else:

        print("wrong username: " + username)

