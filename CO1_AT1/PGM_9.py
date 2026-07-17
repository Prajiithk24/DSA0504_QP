employees = {
    "Rahul": 45000,
    "Priya": 60000,
    "Amit": 55000,
    "Sneha": 75000,
    "Karan": 52000
}

highest = max(employees, key=employees.get)
lowest = min(employees, key=employees.get)
average = sum(employees.values()) / len(employees)

print("Highest Salary Employee:", highest, "-", employees[highest])
print("Lowest Salary Employee:", lowest, "-", employees[lowest])
print("Average Salary:", average)