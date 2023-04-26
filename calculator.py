def add(numbers):
    result = 0
    for num in numbers:
        result += num
    return result

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result /= num
    return result

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num_list = []
        n = int(input("How many numbers do you want to " + ("add", "subtract", "multiply", "divide")[int(choice) - 1] + "? "))
        for i in range(n):
            num_list.append(float(input("Enter number " + str(i + 1) + ": ")))

        if choice == '1':
            print("Result:", add(num_list))

        elif choice == '2':
            print("Result:", subtract(num_list))

        elif choice == '3':
            print("Result:", multiply(num_list))

        elif choice == '4':
            print("Result:", divide(num_list))
        break
    else:
        print("Invalid Input")
