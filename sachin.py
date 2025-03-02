#3A
p = int(input('Enter the principal amount: '))
r= int(input('Enter the rate of interest: '))
t= int(input('Enter the time period: '))
#simple interest
si = (p*r*t)/100
print(f'The interest on {p} is {si}')
#4B
list1=[10,20,40,60]
list2=[400,500,600,700]
list2.reverse()
for i in range(len(list1)):
    print(list1[i],list2[i])
    
#5B
word=input()
vowels=['a','e','i','o','u']
vowel_in_word=''
for i in word:
    if i in vowels:
        vowel_in_word+=i
print(f'Vowels in {word} are {vowel_in_word}')


#2a
a=int(input('Enter the first number: '))
t=(12,23,34,45,56,67,78,89,90)
if a in t:
    # print(f'The index of {a} is {t.index(a)}')
    b=list(t)
    b.remove(a)
    t=tuple(b)
    print(f'The tuple after removing {a} is {t}')

#febnanci series with function
def febnanci(n):
    if n==1 or n==0:
        return 1
    else:
        return febnanci(n-1)+febnanci(n-2)
n=int(input('Enter the number of terms: '))
print(f'The value of  febnanci series at {n} is {febnanci(n)}')

#febnanci series without function
n=int(input('Enter the number of terms: '))
for i in range(n):
    if i==0 or i==1:
        a,b=0,1
    else:
        a,b=b,a+b
    print(a,end=' ')
    
#bank system with class
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_no):
        if account_no in self.accounts:
            print(f'Account {account_no} already exists.')
        else:
            self.accounts[account_no] = 0
            print(f'Account {account_no} created.')

    def deposit(self, account_no, amount):
        if account_no in self.accounts:
            self.accounts[account_no] += amount
            print(f'Amount {amount} deposited in account {account_no}.')
        else:
            print(f'Account {account_no} does not exist.')
    def display(self, account_no):
        if account_no in self.accounts:
            print(f'The balance of account {account_no} is {self.accounts[account_no]}')
        else:
            print(f'Account {account_no} does not exist.')

# Example usage
bank = Bank()
bank.create_account(101)
bank.deposit(101, 500)
# bank.withdraw(101, 200)
bank.display(101)


#4B

class Quadrilateral:
    def __init__(self, side1, side2, side3, side4):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

    def perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4

class Rectangle(Quadrilateral):
    def __init__(self, length, breadth):
        super().__init__(length, breadth, length, breadth)
        self.length = length
        self.breadth = breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

class Square(Quadrilateral):
    def __init__(self, side):
        super().__init__(side, side, side, side)
        self.side = side

    def perimeter(self):
        return 4 * self.side

# Example usage
rect = Rectangle(10, 5)
print(f'The perimeter of the rectangle is {rect.perimeter()}')

sq = Square(4)
print(f'The perimeter of the square is {sq.perimeter()}')


#for loop for 5b
element=int(input('Enter the number of elements: '))
list1=[]
for i in range(element):
    a=int(input('Enter the element: '))
    print(f'The element is {a} is added at index {i}')
    list1.append(a)
print(f'The list is {list1}')


#given number is prime or not
n=int(input('Enter the number: '))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(f'{n} is not a prime number')
            break
    else:
        print(f'{n} is a prime number')
        
#employee class
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print(f'Name: {self.name}, Emp ID: {self.emp_id}, Salary: {self.salary}')
vicky=Employee('Vicky',101,10000)
vicky.display()

#multiplication matrix
def matrix_multiplication(A, B):
    # Check if matrices can be multiplied
    if len(A[0]) != len(B):
        print("Matrices cannot be multiplied")
        return None

    # Initialize result matrix with zeros
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Perform matrix multiplication
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Example matrices
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Multiply matrices
result = matrix_multiplication(A, B)

#read text file
a=open('text.txt','r')
b=open('text1.txt','w')
content=a.read()
#to store all contents in another file in capital letter
capital_content=content.upper()
b.write(capital_content)
a.close()
b.close()
#to count total no of chareter if file
a=open('text.txt','r')
content=a.read()
count=0
for i in content:
    count+=1
print(f'The total number of characters in file is {count}')
a.close()


#checking given number is palindrome or not
n=int(input('Enter the number: '))
def is_palindrome(n, temp=0):
    if n == 0:
        return temp
    temp = (temp * 10) + (n % 10)
    return is_palindrome(n // 10, temp)

original_n = n
reverse_n = is_palindrome(n)

if original_n == reverse_n:
    print(f'{original_n} is a palindrome')
else:
    print(f'{original_n} is not a palindrome')
    
#n is palindrome or not using function
n=int(input('Enter the number: '))
b=str(n)
if b==b[::-1]:
    print(f'{n} is a palindrome')