num = int(input('Enter the number:'))
if num > 1:
    for i in range(2, num - 1):
        if (num % i) == 0:
            print("The number is not prime")
            break
    else:
        print("The number is prime")

else:
    print("The number is not prime")
