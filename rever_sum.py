'''Q11: Write a program that accepts a three digit number from user
and obtain reverse of the number and then calculate sum of
all the digits.(without using if/ loop)'''

number = (input("Enter a three-digit number: "))

reversed_number = (number[::-1])

digit_sum = int(number[0]) +int (number[1]) +int (number[2])

print("Reversed Number:", reversed_number)
print("Sum of digits:", digit_sum)
