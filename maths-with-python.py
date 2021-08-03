
num1 = int(input("Enter the first number"))
num2 =int(input("Enter the second number"))
choice = input("Enter the operstion to be performed. Available Options:\nadd\nsubtract\ndivision\nmultiply")
outputStatement = input("Enter the output Statement.\nAvailable Variables:\n{output} - The output\n{operation} - The operation performed\n{number1} - The number at 1\n{number2} - The number at 2")
number1 = str(num1)
number2 = str(num2)
if choice == "add":
    sum = num1+num2
    sum = str(sum)
    output = outputStatement.replace("{operation}", choice).replace("{number1}", number1).replace("{number2}", number2).replace("{output}", sum)
    print(output)
elif choice == "subtract":
    diff = num1-num2
    diff = str(sum)
    output = outputStatement.replace("{operation}", choice).replace("{number1}", number1).replace("{number2}", number2).replace("{output}", diff)
    print(output)
elif choice == "division":
    choice2 = input(print("What you want as output? [Available Options: Quotient or Remainder]"))
    if choice2 == "Remainder":
        if num1 < num2:
            first1 = num2
            second1 = num1
            answerr = first1%second1
            answerr = str(answerr)
            output = outputStatement.replace("{operation}", choice).replace("{number1}", number1).replace("{number2}", number2).replace("{output}", answerr)
            print(output)
        else:
            remain = num1%num2
            remain = str(remain)
            output = outputStatement.replace("{operation}", choice).replace("{number1}", number1).replace("{number2}", number2).replace("{output}", remain)
            print(output)
    elif choice2 == "Quotient":
        if num1 < num2:
            first = num2
            second = num1
            answer = first/second
            answer = str(answer)
            output = outputStatement.replace("{operation}", choice).replace("{number1}", number1).replace("{number2}", number2).replace("{output}", answer)
            print(output)
        else:
            qout = num1/num2
            output = outputStatement.replace("{operation}", choice).replace("{number1}", number1).replace("{number2}", number2).replace("{output}", qout)
            print(output)
elif choice == "multiply":
    product = num1*num2
    product = str(product)
    output = outputStatement.replace("{operation}", choice).replace("{number1}", number1).replace("{number2}", number2).replace("{output}", product)
    print(output)
else:
    print("Wrong Choice! Choose an option from these: [add, subtract, multiply, division]")
