#for itemvariable in iterable:
#itemvariable is a variable that takes the value of the item inside the iterable on each iteration.
for item in ["apple", "banana", "cherry"]:
  print(item)
for item in range(5,10,2):
  print(item)
prices=[10, 20, 30]
total=0
for i in prices:
   total+=i
   print(f"total cost is {total}")
    