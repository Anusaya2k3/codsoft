



print("select the option")
print("1--Addition")
print("2--Subraction")
print("3--Multiplication")
print("4--division")
print("5--Exit")

num1= eval(input("Enter the first Number = "))
num2= eval(input("Enter the second Number = "))

while(True):
    choice=int(input("Enter the Choice from(1/2/3/4/5)"))
    if choice in(1,2,3,4,5):
        if choice==1:
            print("Addition of two number ",num1,"and",num2,"is",num1 + num2)
        elif choice==2:
            print("Subraction of two number ",num1,"and",num2,"is",num1 - num2)
        elif choice==3:
            print("multiplication of two number ",num1,"and",num2,"is",num1 * num2)
        elif choice==4:
            print("divition of two number",num1,"and",num2,"is",num1 / num2)
        elif choice==5:
            print("Thank You :)")
            Exit()
    else:
        print("invalid Choice try again")

