number = 9
for i in range(2,number):
    print(i)
    if number % i == 0:
        print("not prime ")
        break
    else:
        print("prime number")
        break