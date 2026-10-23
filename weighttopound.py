weight=input("Enter your weight")
print("(L)bs or (K)g")
unit=input()
if unit.upper()=="L":
    converted=float(weight)*0.45
    print(f"You are {converted} kilos")
if unit.upper()=="K":
    converted=float(weight)//0.45
    print(f"You are {converted} pounds")