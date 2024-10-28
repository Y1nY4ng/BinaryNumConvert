def decimalToBinary(num): 
    Binary = "" 
    while num > 0: 
        Binary = str(num % 2) + Binary 
        num = num // 2 
        return Binary 

userInput = int(input("Enter a number to convert: ")) 
print(decimalToBinary(userInput))