numterms = 10
fibo_list=[]
n1, n2 = 0, 1
count = 0

if numterms <= 0:
    psss
elif numterms == 1:
   fibo_list.append(n1)
else:
   while count < numterms:
       fibo_list.append(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

lower_value = 0
upper_value = 24 
  
primenumbers=[]
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            primenumbers.append(number)


def printNumber(lst, index):
    print(str(lst[index]) + " ", end="")

for i in range(len(primenumbers)+1):
    printNumber(fibo_list, i)
    if len(primenumbers)!=i:
        printNumber(primenumbers, i)
