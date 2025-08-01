n = int(input("Enter any number:"))

for i in range(2, n):
    if(n%i) == 0:
        print("Provided number is not prime!")
        break
else:
    print("Provided number is prime!")

name =str(input("Tell me your name"))
print("My name is:" + name)

