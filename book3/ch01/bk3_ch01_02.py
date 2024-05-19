num = float(input("Enter a number: "))

if num.is_integer():

    if (num % 2) == 0:
        print("{0} is even ".format(int(num)))
    else:
        print("{0} is odd ".format(int(num)))

else:
    print("{0} is not an integer ".format(num))
