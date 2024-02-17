#Write a Simple Calculator in Python with following Operatiors : (+,-,*,/)

#Answer :
#Getting Input from user
#Integer Variables Input
n1=int(input("Enter the 1st Number : "))
n2=int(input("Enter the 2nd Number : "))
#Operator Variable Input
op=str(input("""Choose Operator :
            1: Addition
            2: Subtraction
            3: Multiplication
            4: Division
            
            Choice (1/2/3/4) : """))
#Declaring a Variable for the Output and Calculations
out=None #Output Variable
#Declaring Operations based on Input from user with the help of if-else statement
if op == "1": #Addition
    out=n1+n2
elif op == "2": #Subtraction
    out=n1-n2
elif op == "3": #Multiplication
    out=n1*n2
elif op == "4": #Divison
    out=n1/n2
else:#Fallback Error Statement incase unrecognised input
    print("Error")
print("Output : ",out) #Printing the Output
