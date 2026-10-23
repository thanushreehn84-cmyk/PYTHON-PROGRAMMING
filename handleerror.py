try:
    age=int(input('Age: '))
    income=20000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print('Cannot divide by 0')
except ValueError:
    print("Invalid error")
