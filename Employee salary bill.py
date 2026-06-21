name = input("Enter Employee Name:" )
salary = float(input("Enter Current Salary:" ))

hra = salary * 0.10
da = salary * 0.05
gross = salary + hra + da

print("\n----- Salary slip -----")
print("Employee Name:",name)
print("Current salary:",salary)
print("Gross salary:",gross)
