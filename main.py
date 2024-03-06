stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below   
stdform = stdform.lower()
parts = stdform.split("x")
decimal = parts[0]
exponent = parts[1]
e_notation = (parts[1].split("^"))[1]

print(f"This number in E notation is {decimal}E{e_notation}.")

