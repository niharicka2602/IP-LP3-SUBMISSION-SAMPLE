def degree(input_degree):
    if input_type == "C" or input_type == "c":
        fahrenhite = round((input_degree * 9/5) + 32)
        print(f"{fahrenhite} F")
    if input_type == "F" or input_type == "f":
        celsius = round((input_degree - 32) * 5/9)
        print(f"{celsius} C")
    return None


input_type = input()
input_degree = int(input("Enter the degree : "))
degree(input_degree)