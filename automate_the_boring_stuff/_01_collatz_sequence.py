# Write a function named collatz() that has one parameter named number.
# If number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.

def collatz(number):
    while number > 1:
        if number % 2 == 0:
            number = int(number/2)
            print(number)
        else:
            number = (number*3)+1
            print(number)


try:
    number = int(input("Ingrese un numero entero: "))
    collatz(number)
except ValueError as e:
    print("ERROR. Debe introducir un entero.")
