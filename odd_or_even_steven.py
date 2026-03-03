# num = int(input("enter a number to check!"))
#
# if num % 2 == 0:
#     print("It is Even")
# elif num % 2 != 0:
#     print("It is odd")
# else:
#     print("Please Enter a Number")

for num in range(1,101):
    if  num % 5 == 0 and num % 10 == 0:
        print("fizz my jizz")
    if num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("jizz")
    elif num % 6 == 0:
        print("67 67 67 67 ")
    elif num % 7 == 0:
        pass
    else:
        print(num)


