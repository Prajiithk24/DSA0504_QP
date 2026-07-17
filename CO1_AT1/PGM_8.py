marks = [78, 65, 90, 45, 35, 88, 55, 72]

print("Marks:", marks)
print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))
print("Average Mark:", sum(marks) / len(marks))

passed = 0
for mark in marks:
    if mark >= 40:
        passed += 1

print("Number of Students Passed:", passed)