add=0
for i in range(1,101):
    if i%3==0 and i%5==0:
        add+=i
print(f"The sum of all number between 1 and 100 that are divisible by 3 and 5 is {add}")