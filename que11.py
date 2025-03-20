user=input("Enter a number: ")
for i in range(len(user)//2):
    if user[i]==user[len(user)-1-i]:
        print(f"{user} is a palindrome number")
    else:
        print(f"{user} is not a palindrome number")