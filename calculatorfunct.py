def multiply(num_1 , num_2):
    multiply = num_1 * num_2
    return multiply

def addition(num_1 , num_2):
    addition = num_1 + num_2
    return addition

def subtraction(num_1 , num_2):
    subtraction = num_1 - num_2
    return subtraction

def division(num_1 , num_2):
    division = num_1 // num_2
    return division

num_1 = float(input("input the first number: "))
num_2 = float(input("input the second number: "))


functs = ["multiply" , "addition" , "subtraction" , "division"]
print(functs)

choice = input("Choose a function from the list above: ")
if choice == "multiply":
    multiply = multiply(num_1 , num_2)
    print(multiply)
if choice == "addition":
    addition = addition(num_1 , num_2)
    print(addition)
if choice == "subtraction":
    subtraction = subtraction(num_1 , num_2)
    print(subtraction)
if choice == "division":
    division = division(num_1 , num_2)
    print(division)
        

    
