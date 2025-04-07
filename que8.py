string=input("Enter a string: ")
string_list=[]
for i in range(len(string)-1,-1,-1):
    string_list.append(string[i])
print(*string_list)
    
    