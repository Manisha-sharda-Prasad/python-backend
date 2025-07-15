#🔹 4. Functions (def, return, parameters)------------
#✅ Basic Function:

def greet():
    print("Hello!")

greet()             # Output: Hello!

#✅ Function with Parameters:
def greet(name)-> None:
    print("Hello,", name)

#✅ Function with Parameters + default values:
def greet2(name="Guest"):
    print("Hello", name)

#✅ Function with Return Value:
def add(a, b):
    return a + b

def multiply(x,y):
    return x * y


print('\n🟪',"="*20, 'topic-3 :: function', '='*20)

print("➡️testing function 1 : greet")
greet("Manisha")  # Output: Hello, Manisha

print("➡️testing function 2 : greet2")
greet2()  # Hello Guest
greet2("Anya")  # Hello Anya

print("➡️testing function 3 : add")
result = add(5, 3)
print("Sum:", result)

print("➡️testing function 4 : multiply")
num1 = int(input('enter x: '))
num2  = int(input('enter y: '))
result = multiply(num1, num2)
print("result:", result)
# result = multiply(x=input('enter x'), y=input('enter y'))
# multiply(y=1, x=2)
