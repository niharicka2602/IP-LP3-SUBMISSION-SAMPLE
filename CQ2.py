def leap(input_year):
    if (input_year % 4 == 0 and input_year % 100 != 0 or input_year % 400 == 0):
        print(True)
    else:
        print(False)
    return None

input_year = int(input())
leap(input_year)