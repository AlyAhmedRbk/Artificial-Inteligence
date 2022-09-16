
for i in range(20):
    if i % 3 == 0:
        print(i)
    elif i % 5 == 0:
        print("Bingo !!")
        print("-----")
    else:
        pass

#  Activity Two

inp = input("Enter a Number to check if it is Even or Odd       :")
if int(inp) % 2 == 0:
    print("The Number  "+inp+"  is Even Number")
else:
    print("The Number  "+inp+"  is Odd Number")

#   Activity Three

sum= 0
n = int(input("Enter Any Integer    :"))

while n !=0:
    n = int(input("Enter Any Integer    :"))
    sum=sum+n

print("Sum of the Integers Is    :", sum)
"""

#   Activity Four
"""
isPrime = True
i = 2
n = int(input("Enter a Number   :"))
while i<n:
    rem = n%i
    if rem == 0:
        isPrime = False
        break
    else:
        i = i+1
if isPrime:
    print(n, " is a prime Number   ")
else:
    print(n, " is not a prime Number   ")




sum = 0
i = 1
while i<=5:
    s= int(input("Enter a  Number       :"))
    sum=sum+s
    i=i+1

print("Sum Of the Integers is  :", sum)


sum = 0
i =1
while i<=10:
    print(i)
    sum=sum+i
    i=i+1

print("--------")
print("Sum is ", sum)


num = int(input("Enter A Number      :"))

reversed_num = 0
while num != 0:
     digit = int(num % 10)
     reversed_num = int(reversed_num * 10 + digit)
     num=int(num/10)


print("Reversed Number is  :", reversed_num)



n= 1
while n!=0:
    n = int(input("Enter Number to find it is Even or Odd    :"))
    if n%2==0:
        print("Even Number  !!!")
    elif n%3==0:
        print("Odd Number  !!!")
    else:
        print("-----")
        pass




Total_Marks = float(input('Enter Your Total Marks     :'))
Obt_Marks = float(input('Enter Obtained Marks         :'))
if (Total_Marks  <  Obt_Marks):
    print('Please Enter Valid Marks')
else:
    percentage = float((Obt_Marks/Total_Marks) * 100)
    print('Percentage   :')
    print(percentage)

print('--------------------------------')
print('      Grade')
if (percentage >= 80):
    print('You Have An A+ Grade')
    print('Nice Effort')
elif(percentage >= 70):
    print('You Have An A Grade')
    print('Good! Keep it up')
elif(percentage >= 60):
    print('You Have A B Grade')
    print('Work hard')
elif(percentage >=50):
    print('You Have A C Grade')
    print('Need to work more Hard')
else:
    print('Soory You Have A F Grade')
    print('Please Focus o your work')

inp = int(input("Enter a number to find  :"))
fact=1

while inp !=0:
    fact=fact*inp
    inp= inp-1

print("Factorial Of Number  is  ", fact )


