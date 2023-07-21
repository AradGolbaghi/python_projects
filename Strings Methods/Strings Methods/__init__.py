weight = int(input("Weight: "))
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
    converted = weight * 2.20462262
    print(f"You are {converted} kilograms")
else:
    converted = weight / 2.20462262
    print(f"You are {converted} lbs")
