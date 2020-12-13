#   a114_divisible.py

# get two numbers from user

numbers = input("Enter 2 numbers").split(' ')

# loop whle the numbers are not divisible (the remainder is 0)

while int(numbers[0]) %int(numbers[1])!= 0:
   # inform user of result 

  print('The first number isn\'t divisible')
  # gather user input again

  numbers = input("Enter 2 numbers").split(' ')
# inform user of result
 
print('The first number is divisible')
